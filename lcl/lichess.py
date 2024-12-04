def game_ok_eco(metadata, min_elo):
    return int(metadata["WhiteElo"]) >= min_elo or int(metadata["BlackElo"]) >= min_elo

def game_ok_commented(metadata, min_elo):
    return game_ok_eco(metadata, min_elo)

def init_game_data():
        current_game = []
        game_metadata = {
            "ECO": None,
            "WhiteElo": None,
            "BlackElo": None,
            "Commented": False,
        }
        return current_game, game_metadata

def get_eco_filename(year, month, metadata):
     return metadata["ECO"] + ".pgn"