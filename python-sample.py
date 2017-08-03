def wombat(state, time_left):
	shoot = 'command': { 'action': 'shoot', 'metadata': {} }

     smoke = 'command': { 'action': 'smoke', 'metadata': {'direction' : 'backward' } }

    return {
        'command': { previous == shoot : smoke ? shoot },
        'state': { 'previous': 'state'['saved-state'] == shoot : smoke ? shoot }
    }
