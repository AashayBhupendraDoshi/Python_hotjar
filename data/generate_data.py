# Generate button click data for clustering
# Origin is at [0,0]
import math
import numpy as np


def rectangle(x:float, y:float, l:float,w: float, num_points:int = 100, gaussian: bool=False):
    '''
    Generate clicks for a rectangular button
    Params:
    x,y: coordinates og the center
    l: length of the button (x-axis)
    w: width of the button (y-axis)
    num_points: number of points
    gaussian: if the clicks are geospacially distributed normally of uniformly
    '''

    if x<=0 or x>=1 or y<=0 or y>=1:
        raise Exception("Component out of bounds. Use value between 0 and 1")
    else:
        ll = max(x-l/2,0)
        lh = min(x+l/2,1)
        wl = max(y-w/2,0)
        wh = min(y+w/2,1)
        if gaussian:
            XX = np.random.normal(loc=x, scale=l/2,size=2*num_points)
            YY = np.random.normal(loc=y, scale=w/2,size=2*num_points)
            X = [i for i in XX if ll<=i<=lh]
            if len(X)>num_points:
                X = X[:num_points]
            Y = [i for i in YY if wl<=i<=wh]
            if len(Y)>num_points:
                Y = Y[:num_points]

        else:
            X = np.random.uniform(low=ll, high=lh, size=num_points)
            Y = np.random.uniform(low=wl, high=wh, size=num_points)

        
        return np.array([X,Y])

def circle(x:float, y:float, r:float, num_points:int = 100, gaussian: bool=False):
    '''
    Generate clicks for a rectangular button
    Params:
    x,y: coordinates og the center
    r: radius of the button
    num_points: number of points
    gaussian: if the clicks are geospacially distributed normally of uniformly
    '''

    if x<=0 or x>=1 or y<=0 or y>=1:
        raise Exception("Component out of bounds. Use value between 0 and 1")
    else:
        if gaussian:
            R = np.absolute( np.random.normal(loc=0, scale=r/2, size=2*num_points) )
            r = np.array([i for i in R if i<=r])
            if len(r)>num_points:
                r = r[:num_points]
            
        else:
            r = np.random.uniform(low=0,high=r, size=num_points)


        theta = np.random.uniform(low=0,high=2*math.pi, size=num_points)
        rcos = np.cos(theta)
        rsin = np.sin(theta)
            
    return np.array([x+r*rcos, y+r*rsin])


def noise(num_points:int=50):
    x = np.random.uniform(low=0,high=1, size=num_points)
    y = np.random.uniform(low=0,high=1, size=num_points)

    return np.array([x,y])

# print(rectangle(0.4,0.3,0.4,0.2,10,False))
# print(rectangle(0.4,0.3,0.4,0.2,10,True))
# print(circle(0.2,0.2,0.15,10,False))
# print(circle(0.2,0.2,0.15,10,True))
