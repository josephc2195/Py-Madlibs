import re

template = '''<name> went for a walk at <place>. <he or she>
found a <noun>. <name> decided to take it home.'''

def madlibs(template):
    print('The story template is:\n' + template)
    fields = sorted(set( re.findall('<[^>]+>', template) ))
    values = input('\nInput a list of words to replace the following sections:'
                   '\n  %s: ' % ','.join(fields)).split(' ')
    story = template
    print(fields)
    for f,v in zip(fields, values):
        story = story.replace(f, v)
    print('\nThe story becomes:\n\n' + story)

madlibs(template)
