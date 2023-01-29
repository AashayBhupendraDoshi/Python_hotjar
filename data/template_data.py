import numpy as np
from generate_data import rectangle, circle, noise


def sparce_template():
    # Two rectangle buttons
    # One circular button
    # One scroll
    # 5% misclicks

    # Sparce Template 200points normal
    rec_but_1 = rectangle(0.25,0.25,0.15,0.15,50, True)
    rec_but_2 = rectangle(0.25,0.75,0.15,0.15,50, True)
    cic_but_1 = circle(0.75,0.5,0.1,50,True)
    scroll_1 = rectangle(0.95,0.5,0.025,0.8,50, True)
    noise_1 = noise(10)
    class_50_normal = np.array([0]*50 + [1]*50 + [2]*50 + [3]*50 + [-1]*10)
    sparce_50_normal = np.concatenate((rec_but_1,rec_but_2,cic_but_1,scroll_1, noise_1),axis=1)

    # Sparce template 200points uniform
    rec_but_1 = rectangle(0.25,0.25,0.15,0.15,50, False)
    rec_but_2 = rectangle(0.25,0.75,0.15,0.15,50, False)
    cic_but_1 = circle(0.75,0.5,0.1,50,False)
    scroll_1 = rectangle(0.95,0.5,0.025,0.8,50,False)
    noise_1 = noise(10)
    class_50_uniform = np.array([0]*50 + [1]*50 + [2]*50 + [3]*50 + [-1]*10)
    sparce_50_uniform = np.concatenate((rec_but_1,rec_but_2,cic_but_1,scroll_1, noise_1),axis=1)


    # Sparce Template 4000points normal
    rec_but_1 = rectangle(0.25,0.25,0.2,0.2,1000, True)
    rec_but_2 = rectangle(0.25,0.75,0.2,0.2,1000, True)
    cic_but_1 = circle(0.72,0.5,0.2,1000,True)
    scroll_1 = rectangle(0.97,0.5,0.02,0.8,1000, True)
    noise_1 = noise(200)
    class_1000_normal = np.array([0]*1000 + [1]*1000 + [2]*1000 + [3]*1000 + [-1]*200)
    sparce_1000_normal = np.concatenate((rec_but_1,rec_but_2,cic_but_1,scroll_1, noise_1),axis=1)

    # Sparce Template 4000points uniform
    rec_but_1 = rectangle(0.25,0.25,0.2,0.2,1000, False)
    rec_but_2 = rectangle(0.25,0.75,0.2,0.2,1000, False)
    cic_but_1 = circle(0.72,0.5,0.2,1000,False)
    scroll_1 = rectangle(0.97,0.5,0.02,0.8,1000,False)
    noise_1 = noise(200)
    class_1000_uniform = np.array([0]*1000 + [1]*1000 + [2]*1000 + [3]*1000 + [-1]*200)
    sparce_1000_uniform = np.concatenate((rec_but_1,rec_but_2,cic_but_1,scroll_1, noise_1),axis=1)


    return sparce_50_normal,class_50_normal, sparce_50_uniform, class_50_uniform, sparce_1000_normal, class_1000_normal, sparce_1000_uniform, class_1000_uniform



def dense_template():
    # 12 rectangle buttons
    # 1 circular button
    # 1 scroll
    # 5% misclicks
    # Gaussian
    # Random clicks for every button

    cir_but_1 = circle(0.05, 0.95, 0.04, 1000, True)
    # Sidebar
    rec_but_1 = rectangle(0.1, 0.75, 0.2,0.08,1000, True)
    rec_but_2 = rectangle(0.1, 0.65, 0.2,0.08,1000, True)
    rec_but_3 = rectangle(0.1, 0.55, 0.2,0.08,1000, True)
    rec_but_4 = rectangle(0.1, 0.45, 0.2,0.08,1000, True)
    rec_but_5 = rectangle(0.1, 0.35, 0.2,0.08,1000, True)
    
    # Verticalbar
    rec_but_11 = rectangle(0.4, 0.95, 0.12,0.08,1000, True)
    rec_but_12 = rectangle(0.55, 0.95, 0.12,0.08,1000, True)
    rec_but_13 = rectangle(0.7, 0.95, 0.12,0.08,1000, True)
    rec_but_14 = rectangle(0.85, 0.95, 0.12,0.08,1000, True)

    # Center
    center_screen = rectangle(0.6,0.55,0.6,0.6, 2000, True)
    # Bottom Section
    bottom_section = rectangle(0.6,0.1,0.6, 0.1, 1000, True)
    # Scroll
    scroll_button = rectangle(0.975,0.55,0.02,0.9,1000, True)

    # Noise
    noise_1 = noise(600)

    class_dense_template = []
    for i in range(13):
        if i==10:
            class_dense_template+=[i]*2000
            continue
        class_dense_template+=[i]*1000

    class_dense_template=np.array(class_dense_template+[-1]*600)
    clicks_dense_template = np.concatenate((cir_but_1,
                                            rec_but_1,
                                            rec_but_2,
                                            rec_but_3,
                                            rec_but_4,
                                            rec_but_5,
                                            rec_but_11,
                                            rec_but_12,
                                            rec_but_13,
                                            rec_but_14,
                                            center_screen,
                                            bottom_section,
                                            scroll_button,
                                            noise_1),
                                            axis=1
                                            )

    return clicks_dense_template, class_dense_template

