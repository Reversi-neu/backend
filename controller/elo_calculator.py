def eloCalculator(player_elo, enemy_elo, player_score, enemy_score):
    # Variables to customize elo gains and loses
    diff = 400
    change = 32
    
    expected_score = 1/(1 + (10 ** ((enemy_elo - player_elo) / diff)))

    if player_score > enemy_score:
        game_outcome = 1
    else:
        game_outcome = 0
        
    return int(player_elo + (change * (game_outcome - expected_score)))
