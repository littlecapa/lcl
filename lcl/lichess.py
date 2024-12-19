def game_ok_eco(metadata, min_elo):
    return int(metadata["WhiteElo"]) >= min_elo or int(metadata["BlackElo"]) >= min_elo

def game_ok_commented(metadata, min_elo):
    if metadata["Commented"] == True:
        return game_ok_eco(metadata, min_elo)
    return False

def ignore_event(metadata):
    if metadata["Event"] is not None:
        if "BULLET" in metadata["Event"].upper():
            return True
    return False

def eco_ok(metadata):
     if metadata["ECO"] == "?":
        return False
     return True

def init_game_data():
        current_game = []
        game_metadata = {
            "ECO": None,
            "WhiteElo": None,
            "BlackElo": None,
            "Event": None,
            "Commented": False,
        }
        return current_game, game_metadata

def get_eco_filename(year, month, metadata):
     return metadata["ECO"] + ".pgn"