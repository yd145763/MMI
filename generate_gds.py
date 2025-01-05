# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 15:22:45 2025

@author: limyu
"""

import klayout.db as pya


widthS = [40]
heightS = [20]
pitchS = [0.6]
gapS = [5]
taper_widthS = [5]
waveguide_widthS = [0.5]
taper_lengthS = [10]
taper_pitchS = [0.6]

for w in widthS:
    for h in heightS:
        for p in pitchS:
            for g in gapS:
                for tw in taper_widthS:
                    for wgw in waveguide_widthS:
                        for tl in taper_lengthS:
                            for tp in taper_pitchS:

                                width = w
                                height = h
                                pitch = p
                                gap = g
                                taper_width = tw
                                waveguide_width = wgw
                                taper_length = tl
                                taper_pitch = tp
                                
                                width_str = str(int(width*1000))
                                height_str = str(int(height*1000))
                                pitch_str = str(int(pitch*1000))
                                gap_str = str(int(gap*1000))
                                taper_width_str = str(int(taper_width*1000))
                                waveguide_width_str = str(int(waveguide_width*1000))
                                taper_length_str = str(int(taper_length*1000))
                                taper_pitch_str = str(int(taper_pitch*1000))
                                filename = "w"+width_str+"_"+"h"+height_str+"_"+"p"+pitch_str+"_"+"g"+gap_str+"_"+"tw"+taper_width_str+"_"+"wgw"+waveguide_width_str+"_"+"tl"+taper_length_str+"_"+"tp"+taper_pitch_str+"_"+"end"
                                
                                
                                
                                
                                
                                if 4*pitch>width:
                                    print("Please increase the width of the rectangle or decrease the size of the pitch")
                                    
                                elif 4*taper_pitch>taper_length:
                                    print("Please increase the length of the taper or decrease the size of the taper pitch")
                                
                                if ((2*taper_width)+gap)>height:
                                    print("Please increase the height or decrease the taper width")
                                
                                else:
                                    # Create a new layout
                                    layout = pya.Layout()
                                
                                    # Create a new layer
                                    layer_index = layout.layer(1, 0)  # Layer 1, datatype 0
                                
                                    # Create a top-level cell
                                    top_cell = layout.create_cell(filename)
                                    
                                    
                                    #===========inserting the rectangle===================
                                    #right rectangle
                                    print("right rectangle")
                                    x1 = 0
                                    y1 = -(height/2)
                                    x2 = x1 + (pitch/4)
                                    y2 = height/2
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell.shapes(layer_index).insert(db_rect)
                                    print(x1,x2, "First rectangle")
                                    
                                    x1 = 0.75*pitch
                                    y1 = -(height/2)
                                    x2 = x1 + (pitch/2)
                                    y2 = height/2
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell.shapes(layer_index).insert(db_rect)
                                    print(x1,x2, "second rectangle")
                                    
                                    while x2 <((width/2) - (2*pitch)):
                                        x1 += pitch
                                        y1 = -1*(0.5*height)
                                        x2 = x1+(0.5*pitch)
                                        y2 = 0.5*height
                                        # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                        rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                        # Convert to database units and add it to the layout
                                        db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                        top_cell.shapes(layer_index).insert(db_rect)
                                        print(x1,x2, "following rectangles")
                                    
                                    
                                    margin = (width/2) - x2 
                                    
                                    if margin > pitch and margin < 2*pitch:
                                    
                                        x1 = x1 +pitch
                                        y1 = -1*(height/2)
                                        x2 = (width/2)
                                        y2 = height/2
                                        
                                        # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                        rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                        
                                        # Convert to database units and add it to the layout
                                        db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                        top_cell.shapes(layer_index).insert(db_rect)
                                        print(x1,x2, "final rectangle")
                                    
                            
                                    
                                    
                                    #left rectangle
                                    print("left rectangle")
                                    x1 = 0
                                    y1 = -(height/2)
                                    x2 = x1 - (pitch/4)
                                    y2 = height/2
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell.shapes(layer_index).insert(db_rect)
                                    print(x1,x2, "First rectangle")
                                    
                                    x1 = -1*(0.75*pitch)
                                    y1 = -(height/2)
                                    x2 = (x1 - (pitch/2))
                                    y2 = height/2
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell.shapes(layer_index).insert(db_rect)
                                    print(x1,x2, "second rectangle")
                                    
                                    while x2 >-1*((width/2)- (2*pitch)):
                                        x1 -= pitch
                                        y1 = -1*(0.5*height)
                                        x2 = x1-(0.5*pitch)
                                        y2 = 0.5*height
                                        # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                        rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                        # Convert to database units and add it to the layout
                                        db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                        top_cell.shapes(layer_index).insert(db_rect)
                                        print(x1,x2, "following rectangles")
                                    
                            
                                    
                                    margin = (width/2) + x2 
                                    
                                    if margin > pitch and margin < 2*pitch:
                                    
                                        x1 = x1 - pitch
                                        y1 = -1*(height/2)
                                        x2 = -1*(width/2)
                                        y2 = height/2
                                        
                                        # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                        rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                        
                                        # Convert to database units and add it to the layout
                                        db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                        top_cell.shapes(layer_index).insert(db_rect)
                                        print(x1,x2, "final rectangle")
                            
                                            
                                    #======================merging cell=============================
                                    height_coor_pos = (height/2)*1000
                                    height_coor_neg = -1*((height/2)*1000)
                                    width_coor_pos = (pitch/4)*1000
                                    width_coor_neg = -1*((pitch/4)*1000)
                                    
                                    # Define the two polygons to merge (by their coordinates)
                                    polygon1 = pya.Polygon([pya.Point(0, height_coor_neg), pya.Point(0, height_coor_pos), pya.Point(width_coor_pos, height_coor_pos), pya.Point(width_coor_pos, height_coor_neg)])
                                    polygon2 = pya.Polygon([pya.Point(width_coor_neg, height_coor_neg), pya.Point(width_coor_neg, height_coor_pos), pya.Point(0, height_coor_pos), pya.Point(0, height_coor_neg)])
                                    
                                    # Create a region for the polygons
                                    region = pya.Region()
                                    region.insert(polygon1)
                                    region.insert(polygon2)
                                    
                                    # Merge the two polygons
                                    merged_region = region.merged()
                                    # Replace the original polygons in the layout with the merged result
                                    shapes = top_cell.shapes(layer_index)
                                    shapes.insert(merged_region)
                                    
                                    # Remove the specific polygons from the cell
                                    shapes = top_cell.shapes(layer_index)
                                    for shape in shapes:
                                        if shape.is_polygon:
                                            if shape.polygon == polygon1 or shape.polygon == polygon2:
                                                shapes.erase(shape)
                                    
                                    
                                    #===========inserting the tapers===================
                                    
                                    #m1 always positive, m2 always negative; x1 x3 always follow m1, x2 x4 always follow m2
                                    
                                    gap = gap
                                    taper_width = taper_width
                                    waveguide_width = waveguide_width
                                    taper_length = taper_length
                                    taper_pitch = taper_pitch
                                    
                                    print("upper left arm")
                                    # upper left arm
                                    m1 = ((taper_width/2) - (waveguide_width/2))/(taper_length+(pitch))
                                    x1 = (-1*(width/2)) - (taper_pitch/2)
                                    y1 = (gap/2)+ taper_width
                                    c1 = y1- (m1*x1)
                                    
                                    x2 = x1
                                    y2 = gap/2
                                    m2 = -1*m1
                                    c2 = y2- (m2*x2)
                                    
                                    def linear(x, c, m):
                                        y = (m*x)+c
                                        return y
                                    
                                    x3 = x1 - (taper_pitch/2)
                                    y3 = linear(x3, c1, m1)
                                    x4 = x3
                                    y4 = linear(x4, c2, m2)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                    
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                    
                                    # Add the trapezium to the layer in the top cell
                                    top_cell.shapes(layer_index).insert(trapezium)
                                    print('first trapezium')
                                    
                                    while x4 > (-1)*((width/2)+(taper_pitch/2)+(taper_length) - (2*taper_pitch)):
                                        x1 -= taper_pitch
                                        y1 = linear(x1, c1, m1)
                                        x2 = x1
                                        y2 = linear(x2, c2, m2)
                                        x3 = x1 - (taper_pitch/2)
                                        y3 = linear(x3, c1, m1)
                                        x4 = x3
                                        y4 = linear(x4, c2, m2)
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                    
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                    
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print(x4, 'following trapezium')
                                    
                                    margin = x4 - (-1)*((width/2)+(taper_pitch/2)+(taper_length))
                                    
                                    if margin > taper_pitch and margin < 2*taper_pitch:
                                        x1 = x1 - (taper_pitch)
                                        y1 = linear(x1, c1, m1)
                                        x2 = x1
                                        y2 = linear(x2, c2, m2)
                                        x3 = -1*((0.5*width)+(0.5*taper_pitch)+taper_length)
                                        y3 = (0.5*gap)+(0.5*taper_width)+(0.5*waveguide_width)
                                        x4 = x3
                                        y4 = (0.5*gap)+(0.5*taper_width)-(0.5*waveguide_width)
                                        
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                        
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                        
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print('final trapezium')
                            
                                    
                                    
                                    print("lower left arm")
                                    # lower left arm
                                    m1 = ((taper_width/2) - (waveguide_width/2))/(taper_length+(pitch))
                                    x1 = (-1*(width/2)) - (taper_pitch/2)
                                    y1 = -1*(gap/2)
                                    c3 = y1- (m1*x1)
                                    
                                    x2 = x1
                                    y2 = -1*((gap/2)+(taper_width))
                                    m2 = -1*m1
                                    c4 = y2- (m2*x2)
                                    
                                    
                                    x3 = x1 - (taper_pitch/2)
                                    y3 = linear(x3, c3, m1)
                                    x4 = x3
                                    y4 = linear(x4, c4, m2)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                    
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                    
                                    # Add the trapezium to the layer in the top cell
                                    top_cell.shapes(layer_index).insert(trapezium)
                                    print('first trapezium')
                                    
                                    while x4 > (-1)*((width/2)+(taper_pitch/2)+(taper_length) - (2*taper_pitch)):
                                        x1 -= taper_pitch
                                        y1 = linear(x1, c3, m1)
                                        x2 = x1
                                        y2 = linear(x2, c4, m2)
                                        x3 = x1 - (taper_pitch/2)
                                        y3 = linear(x3, c3, m1)
                                        x4 = x3
                                        y4 = linear(x4, c4, m2)
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                    
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                    
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print(x4, 'following trapezium')
                                    
                                    margin = x4 - (-1)*((width/2)+(taper_pitch/2)+(taper_length))
                                    
                                    if margin > taper_pitch and margin < 2*taper_pitch:
                                        x1 = x1 - (taper_pitch)
                                        y1 = linear(x1, c3, m1)
                                        x2 = x1
                                        y2 = linear(x2, c4, m2)
                                        x3 = -1*((0.5*width)+(0.5*taper_pitch)+taper_length)
                                        y3 = 0-(0.5*gap)-(0.5*taper_width)+(0.5*waveguide_width)
                                        x4 = x3
                                        y4 = 0-(0.5*gap)-(0.5*taper_width)-(0.5*waveguide_width)
                                        
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                        
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                        
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print('final trapezium')
                                    
                                    
                                    #==================================================================================================
                                    #m1 always positive, m2 always negative; x1 x3 always follow m1, x2 x4 always follow m2
                                    
                                    print("upper right arm")
                                    # upper right arm
                                    m1 = ((taper_width/2) - (waveguide_width/2))/(taper_length+(pitch))
                                    x1 = (width/2) + (taper_pitch/2)
                                    y1 = (gap/2)
                                    c1 = y1- (m1*x1)
                                    
                                    x2 = x1
                                    y2 = gap/2 +taper_width
                                    m2 = -1*m1
                                    c2 = y2- (m2*x2)
                                    
                                    def linear(x, c, m):
                                        y = (m*x)+c
                                        return y
                                    
                                    x3 = x1 + (taper_pitch/2)
                                    y3 = linear(x3, c1, m1)
                                    x4 = x3
                                    y4 = linear(x4, c2, m2)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                    
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                    
                                    # Add the trapezium to the layer in the top cell
                                    top_cell.shapes(layer_index).insert(trapezium)
                                    print('first trapezium')
                                    
                                    
                                    
                                    while x4 < ((width/2)+(taper_pitch/2)+(taper_length) - (2*taper_pitch)):
                                        x1 += taper_pitch
                                        y1 = linear(x1, c1, m1)
                                        x2 = x1
                                        y2 = linear(x2, c2, m2)
                                        x3 = x1 + (taper_pitch/2)
                                        y3 = linear(x3, c1, m1)
                                        x4 = x3
                                        y4 = linear(x4, c2, m2)
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                    
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                    
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print(x4, 'following trapezium')
                                    
                                    
                                    margin = ((width/2)+(taper_pitch/2)+(taper_length)) - x4
                                    
                                    if margin > taper_pitch and margin < 2*taper_pitch:
                                    
                                        x1 = x1 + (taper_pitch)
                                        y1 = linear(x1, c1, m1)
                                        x2 = x1
                                        y2 = linear(x2, c2, m2)
                                        x3 = ((0.5*width)+(0.5*taper_pitch)+taper_length)
                                        y3 = (0.5*gap)+(0.5*taper_width)-(0.5*waveguide_width)
                                        x4 = x3
                                        y4 = (0.5*gap)+(0.5*taper_width)+(0.5*waveguide_width)
                                        
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                        
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                        
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print(x1, 'final trapezium')
                                    
                                    
                                    
                                    
                                    #m1 always positive, m2 always negative; x1 x3 always follow m1, x2 x4 always follow m2
                                    
                                    print("lower right arm")
                                    # lower right arm
                                    m1 = ((taper_width/2) - (waveguide_width/2))/(taper_length+(pitch))
                                    x1 = (width/2) + (taper_pitch/2)
                                    y1 = -1*((gap/2)+taper_width)
                                    c3 = y1- (m1*x1)
                                    
                                    x2 = x1
                                    y2 = -1*(gap/2) 
                                    m2 = -1*m1
                                    c4 = y2- (m2*x2)
                                    
                                    def linear(x, c, m):
                                        y = (m*x)+c
                                        return y
                                    
                                    x3 = x1 + (taper_pitch/2)
                                    y3 = linear(x3, c3, m1)
                                    x4 = x3
                                    y4 = linear(x4, c4, m2)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                    
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                    
                                    # Add the trapezium to the layer in the top cell
                                    top_cell.shapes(layer_index).insert(trapezium)
                                    print('first trapezium')
                                    
                                    
                                    
                                    
                                    while x4 < ((width/2)+(taper_pitch/2)+(taper_length) - (2*taper_pitch)):
                                        x1 += taper_pitch
                                        y1 = linear(x1, c3, m1)
                                        x2 = x1
                                        y2 = linear(x2, c4, m2)
                                        x3 = x1 + (taper_pitch/2)
                                        y3 = linear(x3, c3, m1)
                                        x4 = x3
                                        y4 = linear(x4, c4, m2)
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                    
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                    
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print(x4, 'following trapezium')
                            
                                    margin = ((width/2)+(taper_pitch/2)+(taper_length)) - x4
                                    
                                    if margin > taper_pitch and margin < 2*taper_pitch:
                                        x1 = x1 + (taper_pitch)
                                        y1 = linear(x1, c3, m1)
                                        x2 = x1
                                        y2 = linear(x2, c4, m2)
                                        x3 = ((0.5*width)+(0.5*taper_pitch)+taper_length)
                                        y3 = -1*((0.5*gap)+(0.5*taper_width)+(0.5*waveguide_width))
                                        x4 = x3
                                        y4 = -1*((0.5*gap)+(0.5*taper_width)-(0.5*waveguide_width))
                                        
                                        vertices = [
                                            pya.DPoint(x1, y1),  # Point 1
                                            pya.DPoint(x2, y2), # Point 2
                                            pya.DPoint(x4, y4),    # Point 4
                                            pya.DPoint(x3, y3)      # Point 3
                                        ]
                                        
                                        # Create a DPolygon using the vertices
                                        trapezium = pya.DPolygon(vertices)
                                        
                                        # Add the trapezium to the layer in the top cell
                                        top_cell.shapes(layer_index).insert(trapezium)
                                        print(x1, 'final trapezium')
                            
                                    
                                    # Save the layout to a file
                                    layout.write(filename+".gds")
                                    
                                    print("Rectangle created and saved to "+filename+".gds")
                                    
                                                                       
                                    
                                    # Create a new layout
                                    layout0 = pya.Layout()
                                
                                    # Create a new layer
                                    layer_index0 = layout0.layer(1, 0)  # Layer 1, datatype 0
                                
                                    # Create a top-level cell
                                    top_cell0 = layout0.create_cell(filename+"_base")
                                    
                                    x1 = -(width/2)
                                    y1 = -(height/2)
                                    x2 = (width/2)
                                    y2 = height/2
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell0.shapes(layer_index0).insert(db_rect)
                                    print(x1,x2, "Base rectangle")
                                    
                                    x1 = (-width/2)+(-taper_pitch/2)
                                    y1 = (gap/2)
                                    x2 = (-width/2)
                                    y2 = (gap/2)+(taper_width)
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell0.shapes(layer_index0).insert(db_rect)
                                    print(x1,x2, "Upper left rectangle")
                                    
                                    
                                    x1 = (-taper_pitch/2)+(-taper_length)+(-width/2)
                                    y1 = (gap/2)+(taper_width/2)-(waveguide_width/2)
                                    x2 = (-taper_pitch/2)+(-width/2)
                                    y2 = (gap/2)
                                    x3 = (-taper_pitch/2)+(-taper_length)+(-width/2)
                                    y3 = (gap/2)+(taper_width/2)+(waveguide_width/2)
                                    x4 = (-taper_pitch/2)+(-width/2)
                                    y4 = (gap/2)+(taper_width)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                
                                    # Add the trapezium to the layer in the top cell
                                    top_cell0.shapes(layer_index0).insert(trapezium)
                                    print(x1,x2, "Upper left arm")
                                    
                                    
                                    x1 = (-width/2)+(-taper_pitch/2)
                                    y1 = (-gap/2)+(-taper_width)
                                    x2 = (-width/2)
                                    y2 = (-gap/2)
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell0.shapes(layer_index0).insert(db_rect)
                                    print(x1,x2, "Lower left rectangle")
                                    
                                    
                                    x1 = (-taper_pitch/2)+(-taper_length)+(-width/2)
                                    y1 = (-gap/2)+(-taper_width/2)-(-waveguide_width/2)
                                    x2 = (-taper_pitch/2)+(-width/2)
                                    y2 = (-gap/2)
                                    x3 = (-taper_pitch/2)+(-taper_length)+(-width/2)
                                    y3 = (-gap/2)+(-taper_width/2)+(-waveguide_width/2)
                                    x4 = (-taper_pitch/2)+(-width/2)
                                    y4 = (-gap/2)+(-taper_width)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                
                                    # Add the trapezium to the layer in the top cell
                                    top_cell0.shapes(layer_index0).insert(trapezium)
                                    print(x1,x2, "Lower left arm")
                                    
                                    
                                    x1 = (width/2)
                                    y1 = (gap/2)
                                    x2 = (width/2)+(taper_pitch/2)
                                    y2 = (gap/2)+(taper_width)
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell0.shapes(layer_index0).insert(db_rect)
                                    print(x1,x2, "Upper right rectangle")
                                    
                                    x1 = (taper_pitch/2)+(width/2)
                                    y1 = (gap/2)
                                    x2 = (taper_pitch/2)+(width/2)+(taper_length)
                                    y2 = (gap/2)+(taper_width/2)-(waveguide_width/2)
                                    x3 = (taper_pitch/2)+(width/2)
                                    y3 = (gap/2)+(taper_width)
                                    x4 = (taper_pitch/2)+(width/2)+(taper_length)
                                    y4 = (gap/2)+(taper_width/2)+(waveguide_width/2)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                
                                    # Add the trapezium to the layer in the top cell
                                    top_cell0.shapes(layer_index0).insert(trapezium)
                                    print(x1,x2, "Upper right arm")
                                    
                                    x1 = (width/2)
                                    y1 = (-gap/2)+(-taper_width)
                                    x2 = (width/2)+(taper_pitch/2)
                                    y2 = (-gap/2)
                                    # Define rectangle dimensions (x1, y1, x2, y2) in database units (e.g., nanometers)
                                    rect = pya.DBox(x1, y1, x2, y2)  # Rectangle from (0, 0) to (1000, 2000)
                                    
                                    # Convert to database units and add it to the layout
                                    db_rect = pya.DPolygon(rect)  # Convert to database polygon
                                    top_cell0.shapes(layer_index0).insert(db_rect)
                                    print(x1,x2, "Lower right rectangle")
                                    
                                    x1 = (taper_pitch/2)+(width/2)
                                    y1 = (-gap/2)+(-taper_width)
                                    x2 = (taper_pitch/2)+(width/2)+(taper_length)
                                    y2 = (-gap/2)+(-taper_width/2)-(waveguide_width/2)
                                    x3 = (taper_pitch/2)+(width/2)
                                    y3 = (-gap/2)
                                    x4 = (taper_pitch/2)+(width/2)+(taper_length)
                                    y4 = (-gap/2)+(-taper_width/2)+(waveguide_width/2)
                                    
                                    vertices = [
                                        pya.DPoint(x1, y1),  # Point 1
                                        pya.DPoint(x2, y2), # Point 2
                                        pya.DPoint(x4, y4),    # Point 4
                                        pya.DPoint(x3, y3)      # Point 3
                                    ]
                                
                                    # Create a DPolygon using the vertices
                                    trapezium = pya.DPolygon(vertices)
                                
                                    # Add the trapezium to the layer in the top cell
                                    top_cell0.shapes(layer_index0).insert(trapezium)
                                    print(x1,x2, "Lower right arm")
                                    
                                    
                                    layout0.write(filename+"_base.gds")
                                    
                                    print("Rectangle created and saved to "+filename+"_base.gds")