import string
import os
from .lichess import init_game_data

class PgnFileManager:
    LICHESS_FILE_PATTERN = "lichess_{year}-{month}_{iterator1}{iterator2}"
    STATUS_NO_GAME = 0
    STATUS_HEADER = 1
    STATUS_MOVES = 2
    EVAL_PATTERN = "[%eval "

    def __init__(self, split_folder, eco_folder, commented_folder):
        self.split_folder = split_folder
        self.eco_folder = eco_folder
        self.commented_folder = commented_folder

    def init_game_data(self):
        current_game = []
        game_metadata = {
            "ECO": None,
            "WhiteElo": None,
            "BlackElo": None,
            "Commented": False,
        }
        return current_game, game_metadata

    def read_from_split_files(self, year, month):
        """
        Reads games from split PGN files following the Lichess file naming pattern.
        Yields complete games as PGN strings.
        """
        file_pattern = self.LICHESS_FILE_PATTERN.format(year=year, month=month, iterator1="{iterator1}", iterator2="{iterator2}")
        current_game, game_metadata = init_game_data()
        game_status = self.STATUS_NO_GAME

        try:
            for iterator1 in string.ascii_lowercase:
                for iterator2 in string.ascii_lowercase:
                    file_name = file_pattern.format(iterator1=iterator1, iterator2=iterator2)
                    file_path = os.path.join(self.split_folder, file_name)
                    print(f"New filename: {file_path}")
                    if not os.path.isfile(file_path):
                        print(f"No more files found for {iterator1}{iterator2}. Stopping iteration.")
                        raise StopIteration
                    try:
                        with open(file_path, "r", encoding="utf-8") as file:
                            for line in file:
                                line = line.strip()
                                if line.startswith("["):  # Metadata line
                                    if game_status == self.STATUS_NO_GAME:
                                        game_status = self.STATUS_HEADER
                                    current_game.append(line)
                                    if line.startswith("[ECO"):
                                        game_metadata["ECO"] = line.split('"')[1]  # Get ECO code value
                                    elif line.startswith("[WhiteElo"):
                                        game_metadata["WhiteElo"] = line.split('"')[1]  # Get White Elo value
                                    elif line.startswith("[BlackElo"):
                                        game_metadata["BlackElo"] = line.split('"')[1]  # Get Black Elo value

                                elif line == "" and game_status == self.STATUS_HEADER:  
                                    game_status = self.STATUS_MOVES

                                elif line == "" and game_status == self.STATUS_MOVES:  
                                    # Complete game encountered
                                    if current_game:
                                        yield "\n".join(current_game), game_metadata
                                        current_game, game_metadata = init_game_data()
                                    game_status = self.STATUS_NO_GAME

                                elif game_status == self.STATUS_MOVES:  # Moves and annotations
                                    current_game.append(line)
                                    if self.EVAL_PATTERN in line:
                                        game_metadata["Commented"] = True
                                else:
                                    raise ValueError(f"Unexpected line or status: {line}, Status: {game_status}, Current game: {current_game}")
                    except Exception as e:
                        print(f"Error reading Game {current_game}, {game_metadata}, {game_status}")
                        raise

        except StopIteration:
            # Ensure the last game is yielded if incomplete
            if current_game:
                yield "\n".join(current_game), game_metadata

        except Exception as e:
            print(f"Error reading files: {e}")
            raise

    def __str__(self):
        return "I am the PGN File Manager"
