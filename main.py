import math

class Circle:
    def __init__(self, params) -> None:
        self.params = params
        outline = {'type': '', 'string': '', 'label': '', 'showPoint': True, 'fontSize': ''}
        self.output = {'data': []}
        self.x1 = None
        self.x2 = None
        self.y1 = None
        self.y2 = None
        self.mr1 = None
        self.mr2 = None
        self.mpr1x = None
        self.mpr1y = None
        self.mpr2x = None
        self.mpr2y = None
        self.lx1 = None
        self.ly1 = None

    def radius(self):
        if self.params.var1 == 'n' and self.params.var2 == 'n':
            return []
        
        self.x1 = 5 * math.cos((90 - self.params.var1) * math.pi/180)
        self.y1 = 5 * math.sin((90 - self.params.var1) * math.pi/180)
        
        if self.params.var2 == 'n':
            out = {'type': 'polygon', 'string': f'polygon((0, 0), ({self.x1}, {self.y1}))', 'label': None, 'showPoint': None, 'fontSize': None}
            self.output['data'].append(out)
            return out
        
        self.x2 = 5 * math.cos((90 - self.params.var2) * math.pi/180)
        self.y2 = 5 * math.sin((90 - self.params.var2) * math.pi/180)

        shapes = [{'type': 'polygon', 'string': f'polygon((0, 0), ({self.x1}, {self.y1}))', 'label': None, 'showPoint': None, 'fontSize': None},
                  {'type': 'polygon', 'string': f'polygon((0, 0), ({self.x2}, {self.y2}))', 'label': None, 'showPoint': None, 'fontSize': None}
                  ]
        
        [self.output['data'].append(shape) for shape in shapes]
        
        return shapes


    def radiusLabel(self):
        self.mr1 = self.y1/self.x1
        self.mr2 = self.y2/self.x2       #need to have error catch incase any of these are None

        self.mpr1x = self.x1/2
        self.mpr1y = self.y1/2
        self.mpr2x = self.x2/2
        self.mpr2y = self.y2/2

        if self.mr1 > 0:
            self.lx1 = self.mpr1x + 0.5 * math.cos(math.atan(-1/self.mr1))
            self.ly1 = self.mpr1y - 0.5 * math.sin(math.atan(-1/self.mr1))
        elif self.mr1 < 0:
            self.lx1 = self.mpr1x - 0.5 * math.cos(math.atan(-1/self.mr1))
            self.ly1 = self.mpr1y - 0.5 * math.sin(math.atan(-1/self.mr1))
        elif self.mr1 == 0:
            self.lx1 = self.mpr1x 
            self.ly1 = self.mpr1y - 0.25      
        elif self.x1 == 0:
            self.lx1 = self.mpr1x + 0.25
            self.ly1 = self.mpr1y

        if self.mr2 > 0:
            self.lx2 = self.mpr2x + 0.5 * math.cos(math.atan(-1/self.mr2))
            self.ly2 = self.mpr2y - 0.5 * math.sin(math.atan(-1/self.mr2))
        elif self.mr2 < 0:
            self.lx2 = self.mpr2x - 0.5 * math.cos(math.atan(-1/self.mr2))
            self.ly2 = self.mpr2y - 0.5 * math.sin(math.atan(-1/self.mr2))
        elif self.mr2 == 0:
            self.lx2 = self.mpr2x 
            self.ly2 = self.mpr2y - 0.25      
        elif self.x2 == 0:
            self.lx2 = self.mpr2x + 0.25
            self.ly2 = self.mpr2y


        out1 = {'type': 'point', 'string': f'({self.lx1}, {self.lx2})', }
        out2 = 
        out3 = 
        out4 = 
        out5 = 



class Draw:
    """returns a list of strings to be inputted into Desmos for the required shape and parameters"""
    def __init__(self, shape, params) -> None:
        pass