import math 

def radius(var1, var2):
    if var1 == 'n' and var2 == 'n':
        return []
    
    x1 = 5 * math.cos((90 - var1) * math.pi/180)
    y1 = 5 * math.sin((90 - var1) * math.pi/180)
    
    if var2 == 'n':
        return [f'polygon((0, 0), ({x1}, {y1}))']
    
    x2 = 5 * math.cos((90 - var2) * math.pi/180)
    y2 = 5 * math.sin((90 - var2) * math.pi/180)
    
    return [f'polygon((0, 0), ({x1}, {y1}))', f'polygon((0, 0), ({x2}, {y2}))']