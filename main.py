import math
from helpers import Params

class Circle:
    def __init__(self, params) -> None:
        self.params = params
        outline = {'type': '', 'string': '', 'label': '', 'showPoint': True, 'fontSize': ''}
        self.output = {'data': []}
        self.circleString = 'x^2 + y^2 = 25'
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
        self.insangx1 = None
        self.insangy1 = None
        self.insangx2 = None
        self.insangy2 = None
        self.mch1 = None
        self.mch2 = None 
        self.dx1 = None
        self.dy1 = None
        self.intx1 = None
        self.inty1 = None
        self.arcx1 = None
        self.arcx2 = None
        self.stringenough1 = None
        self.string3or4 = None
        self.xmax1 = None
        self.xmax1 = None
        self.xmin2 = None
        self.pch1 = None
        self.pch2 = None
        self.poi1ab = None

        self.abx1 = None
        self.aby1 = None
        self.bex1 = None
        self.bey2 = None

    def radius(self):
        if self.params.var1 == 'n' and self.params.var2 == 'n':
            return None
        if not self.params.var1 and not self.params.var2:
            return None
        
        self.x1 = 5 * math.cos((90 - self.params.var1) * math.pi/180)
        self.y1 = 5 * math.sin((90 - self.params.var1) * math.pi/180)
        
        if not self.params.var2 or self.params.var2 == 'n':
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
        if self.params.var1 == 'n' and self.params.var2 == 'n':
            return []
        
        
        label3 = None if self.params.var3 == 'n' or not self.params.var3 else self.params.var3
        label5 = None if self.params.var5 == 'n' or not self.params.var5 else self.params.var5
        label6 = None if self.params.var6 == 'n' or not self.params.var6 else self.params.var6

        self.mr1 = self.y1/self.x1
        if self.y2 and self.x2: 
            self.mr2 = self.y2/self.x2
            self.mpr2x = self.x2/2
            self.mpr2y = self.y2/2       
        self.mpr1x = self.x1/2
        self.mpr1y = self.y1/2


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

        if self.params.var2 == 'n' or not self.params.var2:

            if label3:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'({self.lx1}, {self.ly1})', 
                    'label': label3, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
            if label5:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'(0, 0)', 
                    'label': label5, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
            if label6:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'({self.x1}, {self.y1})', 
                    'label': label6, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
            return None
        

        else:
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



            label4 = None if self.params.var4 == 'n' or not self.params.var4 else self.params.var4
            label7 = None if self.params.var7 == 'n' or not self.params.var7 else self.params.var7



            if label3:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'({self.lx1}, {self.ly1})', 
                    'label': label3, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
            if label4:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'({self.lx2}, {self.ly2})', 
                    'label': label4, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
            if label5:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'(0, 0)', 
                    'label': label5, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
            if label6:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'({self.x1}, {self.y1})', 
                    'label': label6, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
            if label7:
                self.output['data'].append(
                    {'type': 'point', 
                    'string': f'({self.x2}, {self.y2})', 
                    'label': label7, 
                    'showPoint': False, 
                    'fontSize': '1.5'})
    
    def inscribedAngle1(self):
        if self.params.var8 == 'n' or not self.params.var8:
            return None
        
        self.insangx1 = 5 * math.cos((90-self.params.var9)* math.pi / 180)
        self.insangy1 = 5 * math.sin((90-self.params.var9)* math.pi / 180)
        self.insangx2 = 5 * math.cos((90-self.params.var10)* math.pi / 180)
        self.insangy2 = 5 * math.sin((90-self.params.var10)* math.pi / 180)
        self.insangx3 = 5 * math.cos((90-self.params.var11)* math.pi / 180)
        self.insangy3 = 5 * math.sin((90-self.params.var11)* math.pi / 180)

        self.mch1 = (self.insangy2 - self.insangy1) / (self.insangx2 - self.insangx1)
        self.mch2 = (self.insangy3 - self.insangy2) / (self.insangx3 - self.insangx2)

        if self.insangx1 > self.insangx2: 
            self.dx1 = ((2.25/((self.mch1 ** 2) + 1)) ** 0.5)
        else:
            self.dx1 = ((2.25/((self.mch1 ** 2) + 1)) ** 0.5) * -1
        
        self.dy1 = self.dx1 * self.mch1
        self.intx1 = self.insangx2 + self.dx1
        self.inty1 = self.insangy2 + self.dy1

        if self.insangx3 > self.insangx2: 
            self.dx2 = ((2.25/((self.mch2 ** 2) + 1)) ** 0.5)
        else:
            self.dx2 = ((2.25/((self.mch2 ** 2) + 1)) ** 0.5) * -1
        
        self.dy2 = self.dx2 * self.mch2
        self.intx2 = self.insangx2 + self.dx2
        self.inty2 = self.insangy2 + self.dy2

        if self.intx1 < self.intx2:
            self.arcx1 = self.intx1
        else:
            self.arcx1 = self.intx2
        
        if self.arcx1 == self.intx2:
            self.arcx2 = self.intx1
        else:
            self.arcx2 = self.intx2



        if ((self.insangy2 < self.insangy1 and self.insangy2 < self.insangy3) or (self.insangy2 > self.nsangy1 and self.insangy2 > self.insangy3)):
            self.stringenough1 = True
        else:
            self.stringenough1 = False


        if self.stringenough1 and self.insangy2 < self.insangy1:
            arc = f"y-({self.insangy2}) = (2.25-(x-({self.insangx2}))^2)^0.5{{{self.arcx1}<=x<={self.arcx2}}}"

        else:
            arc = f"y-({self.insangy2}) = (-1)*(2.25-(x-({self.insangx2}))^2)^0.5{{{self.arcx1}<=x<={self.arcx2}}}"

        chord1 = f'polygon(({self.insangx1}, {self.insangy1}),({self.insangx2}, {self.insangy2}))'
        chord2 = f'polygon(({self.insangx3}, {self.insangy3}),({self.insangx2}, {self.insangy2}))'
        
        

        string1 = {'type': 'polygon', 'string': chord1, 'label': None, 'showPoint': True, 'fontSize': None, "color": "black"}
        string2 = {'type': 'polygon', 'string': chord2, 'label': None, 'showPoint': True, 'fontSize': None, "color": "black"}
        string3 = {'type': 'equation', 'string': arc, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
        
        if self.stringenough1:
            self.output['data'].append(string1)
            self.output['data'].append(string2)
            self.output['data'].append(string3)
            
        else:
            self.output['data'].append(string1)
            self.output['data'].append(string2)
        

        
        ##### One arc not enough ######

            self.xmax1 = self.insangx2 + 1.5
            self.xmin2 = self.insangx2 - 1.5
            self.pch1 = self.xmax1 - .001
            self.pch2 = self.xmin2 + .001
            self.poi1ab = True if self.inty1 > self.inty2 else False

            self.abx1 = self.intx1 if self.poi1ab == 1 else self.intx2
            self.aby1 = self.inty1 if self.poi1ab == 1 else self.inty2
            self.bex1 = self.intx2 if self.abx1 == self.intx1 else self.intx1
            self.bey2 = self.inty2 if self.aby1 == self.inty1 else self.inty1


            string5=f"y-({self.insangy2})=(2.25-(x-({self.insangx2}))^2)^0.5{{{self.abx1}<=x<={self.xmax1}}}"
            string6=f"y-({self.insangy2})=(-1)*(2.25-(x-({self.insangx2}))^2)^0.5{{{self.bex1}<=x<={self.xmax1}}}"
            string7=f"(x-({self.insangx2}))^2+(y-({self.insangy2}))^2=2.25{{x>{self.pch1}}}"
            string8=f"y-({self.insangy2})=(2.25-(x-({self.insangx2}))^2)^0.5{{{self.xmin2}<=x<={self.abx1}}}"
            string9=f"y-({self.insangy2})=(2.25-(x-({self.insangx2}))^2)^0.5{{{self.xmin2}<=x<={self.bex1}}}"
            string10=f"(x-({self.insangx2}))^2+(y-({self.insangy2}))^2=2.25{{x<{self.pch2}}}"

            if self.insangx2 < 0:
                out5 = {'type': 'polygon', 'string': string5, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out6 = {'type': 'polygon', 'string': string6, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out7 = {'type': 'equation', 'string': string7, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                self.output['data'].append(out5)
                self.output['data'].append(out6)
                self.output['data'].append(out7)
            else:
                out8 = {'type': 'polygon', 'string': string8, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out9 = {'type': 'polygon', 'string': string9, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out10 = {'type': 'equation', 'string': string10, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                self.output['data'].append(out8)
                self.output['data'].append(out9)
                self.output['data'].append(out10)

        #### labeling angle measure #####

        ####  ERRORS   ####
        angmeas=0.5*(abs(self.params.var9-self.params.var11))
        vec1len=(1+(self.mch1)**2)**0.5
        vec2len=(1+(self.mch2)**2)**0.5
        uv1x=1/vec1len
        uv1y=self.mch1/vec1len
        uv2x=1/vec2len
        uv2y=self.mch2/vec2len
        uvcx=uv1x+uv2x
        uvcy=uv1y+uv2y

        vec1x = self.insangx1-self.insangx2
        vec1y = self.insangy1-self.insangy2
        vec2x = self.insangx3-self.insangx2
        vec2y = self.insangy3-self.insangy2

        vec1length = (vec1x**2 + vec1y**2) **.5
        vec2length = (vec2x**2 + vec2y**2) **.5
        angbisx = vec2length*vec1x+vec1length*vec2x
        angbisy = vec2length*vec1y+vec1length*vec2y
        angbism = angbisy / angbisx
        dist2lab = 2 if self.insangx2<0 else 2.5

        hd1=((dist2lab**2)/(1+angbism**2))**0.5
        vd1=angbism*hd1
        hd2=(-1)*hd1
        vd2=angbism*hd2
        lx1=self.insangx2+hd1
        ly1=self.insangy2+vd1
        lx2=self.insangx2+hd2
        ly2=self.insangy2+vd2

        locx = lx1 if (lx1**2 + ly1**2) < 25 else lx2
        locy = ly1 if (lx1**2 + ly1**2) < 25 else ly2

        string11 = f"({locx}, {locy})"
        out11 = {'type': 'point', 'string': string11, 'label': f"{angmeas} [degree symbol]", 'showPoint': False, 'fontSize': 1.5, "color": "black"}

        self.output['data'].append(out11)

        return None

    def inscribedAngle2(self):
        if self.params.var16 == 'n' or not self.params.var8:
            return None
        
        self.insangx1 = 5 * math.cos((90-self.params.var17)* math.pi / 180)
        self.insangy1 = 5 * math.sin((90-self.params.var17)* math.pi / 180)
        self.insangx2 = 5 * math.cos((90-self.params.var18)* math.pi / 180)
        self.insangy2 = 5 * math.sin((90-self.params.var18)* math.pi / 180)
        self.insangx3 = 5 * math.cos((90-self.params.var19)* math.pi / 180)
        self.insangy3 = 5 * math.sin((90-self.params.var19)* math.pi / 180)

        self.mch1 = (self.insangy2 - self.insangy1) / (self.insangx2 - self.insangx1)
        self.mch2 = (self.insangy3 - self.insangy2) / (self.insangx3 - self.insangx2)

        if self.insangx1 > self.insangx2: 
            self.dx1 = ((2.25/((self.mch1 ** 2) + 1)) ** 0.5)
        else:
            self.dx1 = ((2.25/((self.mch1 ** 2) + 1)) ** 0.5) * -1
        
        self.dy1 = self.dx1 * self.mch1
        self.intx1 = self.insangx2 + self.dx1
        self.inty1 = self.insangy2 + self.dy1

        if self.insangx3 > self.insangx2: 
            self.dx2 = ((2.25/((self.mch2 ** 2) + 1)) ** 0.5)
        else:
            self.dx2 = ((2.25/((self.mch2 ** 2) + 1)) ** 0.5) * -1
        
        self.dy2 = self.dx2 * self.mch2
        self.intx2 = self.insangx2 + self.dx2
        self.inty2 = self.insangy2 + self.dy2

        if self.intx1 < self.intx2:
            self.arcx1 = self.intx1
        else:
            self.arcx1 = self.intx2
        
        if self.arcx1 == self.intx2:
            self.arcx2 = self.intx1
        else:
            self.arcx2 = self.intx2



        if ((self.insangy2 < self.insangy1 and self.insangy2 < self.insangy3) or (self.insangy2 > self.nsangy1 and self.insangy2 > self.insangy3)):
            self.stringenough1 = True
        else:
            self.stringenough1 = False


        if self.stringenough1 and self.insangy2 < self.insangy1:
            arc = f"y-({self.insangy2}) = (2.25-(x-({self.insangx2}))^2)^0.5{{{self.arcx1}<=x<={self.arcx2}}}"

        else:
            arc = f"y-({self.insangy2}) = (-1)*(2.25-(x-({self.insangx2}))^2)^0.5{{{self.arcx1}<=x<={self.arcx2}}}"

        chord1 = f'polygon(({self.insangx1}, {self.insangy1}),({self.insangx2}, {self.insangy2}))'
        chord2 = f'polygon(({self.insangx3}, {self.insangy3}),({self.insangx2}, {self.insangy2}))'
        
        

        string1 = {'type': 'polygon', 'string': chord1, 'label': None, 'showPoint': True, 'fontSize': None, "color": "black"}
        string2 = {'type': 'polygon', 'string': chord2, 'label': None, 'showPoint': True, 'fontSize': None, "color": "black"}
        string3 = {'type': 'equation', 'string': arc, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
        
        if self.stringenough1:
            self.output['data'].append(string1)
            self.output['data'].append(string2)
            self.output['data'].append(string3)
            
        else:
            self.output['data'].append(string1)
            self.output['data'].append(string2)
        

        
        ##### One arc not enough ######

            self.xmax1 = self.insangx2 + 1.5
            self.xmin2 = self.insangx2 - 1.5
            self.pch1 = self.xmax1 - .001
            self.pch2 = self.xmin2 + .001
            self.poi1ab = True if self.inty1 > self.inty2 else False

            self.abx1 = self.intx1 if self.poi1ab == 1 else self.intx2
            self.aby1 = self.inty1 if self.poi1ab == 1 else self.inty2
            self.bex1 = self.intx2 if self.abx1 == self.intx1 else self.intx1
            self.bey2 = self.inty2 if self.aby1 == self.inty1 else self.inty1


            string5=f"y-({self.insangy2})=(2.25-(x-({self.insangx2}))^2)^0.5{{{self.abx1}<=x<={self.xmax1}}}"
            string6=f"y-({self.insangy2})=(-1)*(2.25-(x-({self.insangx2}))^2)^0.5{{{self.bex1}<=x<={self.xmax1}}}"
            string7=f"(x-({self.insangx2}))^2+(y-({self.insangy2}))^2=2.25{{x>{self.pch1}}}"
            string8=f"y-({self.insangy2})=(2.25-(x-({self.insangx2}))^2)^0.5{{{self.xmin2}<=x<={self.abx1}}}"
            string9=f"y-({self.insangy2})=(2.25-(x-({self.insangx2}))^2)^0.5{{{self.xmin2}<=x<={self.bex1}}}"
            string10=f"(x-({self.insangx2}))^2+(y-({self.insangy2}))^2=2.25{{x<{self.pch2}}}"

            if self.insangx2 < 0:
                out5 = {'type': 'polygon', 'string': string5, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out6 = {'type': 'polygon', 'string': string6, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out7 = {'type': 'equation', 'string': string7, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                self.output['data'].append(out5)
                self.output['data'].append(out6)
                self.output['data'].append(out7)
            else:
                out8 = {'type': 'polygon', 'string': string8, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out9 = {'type': 'polygon', 'string': string9, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                out10 = {'type': 'equation', 'string': string10, 'label': None, 'showPoint': True, 'fontSize': None, "color": "red"}
                self.output['data'].append(out8)
                self.output['data'].append(out9)
                self.output['data'].append(out10)

        #### labeling angle measure #####

        ####  ERRORS   ####
        angmeas=0.5*(abs(self.params.var17-self.params.var19))
        vec1len=(1+(self.mch1)**2)**0.5
        vec2len=(1+(self.mch2)**2)**0.5
        uv1x=1/vec1len
        uv1y=self.mch1/vec1len
        uv2x=1/vec2len
        uv2y=self.mch2/vec2len
        uvcx=uv1x+uv2x
        uvcy=uv1y+uv2y

        vec1x = self.insangx1-self.insangx2
        vec1y = self.insangy1-self.insangy2
        vec2x = self.insangx3-self.insangx2
        vec2y = self.insangy3-self.insangy2

        vec1length = (vec1x**2 + vec1y**2) **.5
        vec2length = (vec2x**2 + vec2y**2) **.5
        angbisx = vec2length*vec1x+vec1length*vec2x
        angbisy = vec2length*vec1y+vec1length*vec2y
        angbism = angbisy / angbisx
        dist2lab = 2 if self.insangx2<0 else 2.5

        hd1=((dist2lab**2)/(1+angbism**2))**0.5
        vd1=angbism*hd1
        hd2=(-1)*hd1
        vd2=angbism*hd2
        lx1=self.insangx2+hd1
        ly1=self.insangy2+vd1
        lx2=self.insangx2+hd2
        ly2=self.insangy2+vd2

        locx = lx1 if (lx1**2 + ly1**2) < 25 else lx2
        locy = ly1 if (lx1**2 + ly1**2) < 25 else ly2

        string11 = f"({locx}, {locy})"
        out11 = {'type': 'point', 'string': string11, 'label': f"{angmeas} [degree symbol]", 'showPoint': False, 'fontSize': 1.5, "color": "black"}

        self.output['data'].append(out11)

        return None

    def chord1(self):
        ch1x= 5*math.cos((90-self.params.var26)*math.pi/180)
        ch1y= 5*math.sin((90-self.params.var26)*math.pi/180)
        ch2x= 5*math.cos((90-self.params.var27)*math.pi/180)
        ch2y= 5*math.sin((90-self.params.var27)*math.pi/180)

        string12 = f"polygon(({ch1x}, {ch1y}), ({ch2x}, {ch2y}))"
        self.output['data'].append(
                    {'type': 'polygon', 
                    'string': string12, 
                    'label': None, 
                    'showPoint': True, 
                    'fontSize': '1.5',
                    'color': 'black'}
                    )
    
    def chord2(self):
        ch1x= 5*math.cos((90-self.params.var28)*math.pi/180)
        ch1y= 5*math.sin((90-self.params.var28)*math.pi/180)
        ch2x= 5*math.cos((90-self.params.var29)*math.pi/180)
        ch2y= 5*math.sin((90-self.params.var29)*math.pi/180)

        string12 = f"polygon(({ch1x}, {ch1y}), ({ch2x}, {ch2y}))"
        self.output['data'].append(
                    {'type': 'polygon', 
                    'string': string12, 
                    'label': None, 
                    'showPoint': True, 
                    'fontSize': '1.5',
                    'color': 'black'}
                    )
    
    def chord3(self):
        ch1x= 5*math.cos((90-self.params.var30)*math.pi/180)
        ch1y= 5*math.sin((90-self.params.var30)*math.pi/180)
        ch2x= 5*math.cos((90-self.params.var31)*math.pi/180)
        ch2y= 5*math.sin((90-self.params.var31)*math.pi/180)

        string12 = f"polygon(({ch1x}, {ch1y}), ({ch2x}, {ch2y}))"
        self.output['data'].append(
                    {'type': 'polygon', 
                    'string': string12, 
                    'label': None, 
                    'showPoint': True, 
                    'fontSize': '1.5',
                    'color': 'black'}
                    )
    
    def arc1(self):
        arc1start = ((90 - self.params.var33) * math.pi / 180) if ((90 - self.params.var33) * math.pi / 180) > 0 else 2 * math.pi + ((90 - self.params.var33) * math.pi / 180)
        arc1end = ((90 - self.params.var34) * math.pi / 180) if ((90 - self.params.var34) * math.pi / 180) > 0 else 2 * math.pi + ((90 - self.params.var33) * math.pi / 180)
        
        string13 = f"r=5{{{arc1start}<theta<{arc1end}}}"

        self.output['data'].append(
                    {'type': 'equation', 
                    'string': string13, 
                    'label': None, 
                    'showPoint': True, 
                    'fontSize': '1.5',
                    'color': self.params.var35}
                    )
        
    def arc2(self):
        arc1start = ((90 - self.params.var35) * math.pi / 180) if ((90 - self.params.var35) * math.pi / 180) > 0 else 2 * math.pi + ((90 - self.params.var35) * math.pi / 180)
        arc1end = ((90 - self.params.var36) * math.pi / 180) if ((90 - self.params.var36) * math.pi / 180) > 0 else 2 * math.pi + ((90 - self.params.var35) * math.pi / 180)
        
        string13 = f"r=5{{{arc1start}<theta<{arc1end}}}"

        self.output['data'].append(
                    {'type': 'equation', 
                    'string': string13, 
                    'label': None, 
                    'showPoint': True, 
                    'fontSize': '1.5',
                    'color': self.params.var37}
                    )
        
    def centralAngle1(self):
        larger = False
        if self.params.var24 == "n":
            return None
        if self.params.var24 == "y1":
            larger = True

        if self.params.var25 == 'deg':
            label = '[degrees symbol]'
        else:
            label = self.params.var25
        
        ca1 = (90-self.params.var1)*math.pi/180
        ca2 = (90-self.params.var2)*math.pi/180

        ca3 = ca1 if ca1 > 0 else 2 * math.pi + ca1
        ca4 = ca2 if ca2 > 0 else 2 * math.pi + ca2
        ca5 = ca3 if ca3 < ca4 else ca4
        ca6 = ca4 if ca5 == ca3 else ca3
        ca7 = ca6
        ca8 = 2*math.pi + ca5

        angm1 = (ca6-ca5)*180/math.pi
        angm2=360-angm1

        if larger:
            lcax2=1.25*math.cos(0.5*(ca8+ca7))
            lcay2=1.25*math.sin(0.5*(ca8+ca7))
            string21 = f"r=1{{{ca7}<theta<{ca8}}}"
            string22 = f"({lcax2}, {lcay2})"
            self.output['data'].append(
                    {'type': 'equation', 
                    'string': string21, 
                    'label': None, 
                    'showPoint': True, 
                    'fontSize': '1.5',
                    'color': 'black'}
                    )
            self.output['data'].append(
                    {'type': 'point', 
                    'string': string22, 
                    'label': f"{angm2} {label}", 
                    'showPoint': False, 
                    'fontSize': '1.5',
                    'color': 'black'}
                    )

            
        else:
            lcax1 = 1.25*math.cos(0.5*(ca6+ca5))
            lcay1 = 1.25*math.sin(0.5*(ca6+ca5))
            string19 = f"r=1{{{ca5}<theta<{ca6}}}"
            string20 = f"({lcax1}, {lcay1})"
            self.output['data'].append(
                    {'type': 'equation', 
                    'string': string19, 
                    'label': None, 
                    'showPoint': True, 
                    'fontSize': '1.5',
                    'color': 'black'}
                    )
            self.output['data'].append(
                    {'type': 'point', 
                    'string': string20, 
                    'label': f"{angm1} {label}", 
                    'showPoint': False, 
                    'fontSize': '1.5',
                    'color': 'black'}
                    )

        
class Draw:
    """returns a list of strings to be inputted into Desmos for the required shape and parameters"""
    def __init__(self, params) -> None:
        pass

import json
def main():
    f = open('params.json')
    params_json = json.load(f)
    params = Params(params_json)
    newCircle = Circle(params)
    newCircle.inscribedAngle1()
    print(newCircle.output)


if __name__ == "__main__":
    main()