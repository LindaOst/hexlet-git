def get_event_date(event):
    return event.date 
def current_users(events):
    events.sort(key=get_event_date)
    mashines = {}
    for event in events:
        if event.mashine not in mashines:
            mashines[event.mashine] = set()
        if event.type = "login": 
            mashines[event.mashine].add(event.user)
        elif event.type = 'logout':
            mashines[event.mashine].remove(event.user)
    return mashines
def generate_report(mashines):
    for mashine, users in mashines.items():
        if len(users) > 0:
            user_list = ",".join(users)
            print('{}:{}'.format(mashine, user_list))       
                
    
