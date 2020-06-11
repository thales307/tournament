def tally(rows):
    scores = {
        'win': 3,
        'draw': 1,
        'loss': 0
    }
    HEADER = '{0:<30} |{1[MP]:>3} |{1[W]:>3} |{1[D]:>3} |{1[L]:>3} |{1[P]:>3}'

    def printTable(tableData):
        table = [HEADER.format('Team', {'MP': 'MP', 'W': 'W', 'D': 'D', 'L': 'L', 'P': 'P'})]
        
        for teamName, teamResults in tableData:
            table.append(HEADER.format(teamName, teamResults))
        return table
    
    def addGame(teams, team, result):
        if not team in teams.keys():
            teams[team] = {'MP': 0, 'W': 0, 'D':0, 'L':0, 'P':0}
        teams[team]['MP'] += 1
        teams[team]['P'] += scores[result]
        teams[team]['W'] += (result == 'win')
        teams[team]['D'] += (result == 'draw')
        teams[team]['L'] += (result == 'loss')        
        return teams
    
    teams = {}
    
    for row in rows:
        team1, team2, result = row.split(';')
        if result == 'win':
            teams = addGame(teams, team1, 'win')
            teams = addGame(teams, team2, 'loss')
        elif result == 'loss':
            teams = addGame(teams, team1, 'loss')
            teams = addGame(teams, team2, 'win')
        else:
            teams = addGame(teams, team1, 'draw')
            teams = addGame(teams, team2, 'draw')
            
    teams = sorted(teams.items(), key=lambda x:x[0])
    teams = sorted(teams, key= lambda x: -x[1]['P'])
    table = printTable(teams)
    return table