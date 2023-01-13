import numpy as np


def pretty_depth(depth):
    #Converts depth into a 'nicer' format for display

    
    np.clip(depth, 0, 2**10 - 1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth


def pretty_depth_cv(depth):
    #Converts depth into a 'nicer' format for display

    
    return pretty_depth(depth)


def video_cv(video):
    #Converts video into a BGR format for display

    
    return video[:, :, ::-1]  # RGB -> BGR
