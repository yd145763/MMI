# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:37:19 2025

@author: Lim Yudian
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 18:09:20 2025

@author: Lim Yudian
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import imp
from matplotlib.ticker import StrMethodFormatter

port1_list = []
port2_list = []
port3_list = []
port4_list = []
port1T_list = []
port2T_list = []
port3T_list = []
port4T_list = []
port1base_list = []
port2base_list = []
port3base_list = []
port4base_list = []
port1Tbase_list = []
port2Tbase_list = []
port3Tbase_list = []
port4Tbase_list = []
width_list = []
height_list = []
taper_length_list = []
taper_pitch_list = []
gap_list = []
taper_width_list = []
waveguide_width_list = []
pitch_list = []

fdtd_margin = 5e-06
fdtd_margin_z = 1e-06
soi_thickness = 0.22e-6
etch_depth = 0.11e-6



# Specify the path
path = 'C:\\Users\\Lim Yudian\\Documents\\mmi_gratings\\'

# Get a list of all files in the directory
files = os.listdir(path)

# Filter the GDS files and extract their names without the extension
gds_files = [filename[:-4] for filename in files if filename.endswith('end.gds')]
gds_files_base = [filename[:-9] for filename in files if filename.endswith('base.gds')]

os.add_dll_directory("C:\\Program Files\\Lumerical\\v241\\api\\python\\lumapi.py") #the lumapi.py path in your pc, remember the double \\
lumapi = imp.load_source("lumapi","C:\\Program Files\\Lumerical\\v241\\api\\python\\lumapi.py") #the lumapi.py path in your pc, remember the double \\
    
fdtd = lumapi.FDTD()

import re
g = "w40000_h20000_p600_g5000_tw5000_wgw500_tl10000_tp600_end"

if g in gds_files_base:
    def extractfromstring(symbol, filename):
        match = re.search(symbol+'(\\d+)_', filename)
        if match:
            number = match.group(1)
            number = int(number)
            in_micron = number/1000
            for_fdtd = in_micron*1e-6
            return for_fdtd
    
    width = extractfromstring('w', g)
    width_list.append(width)
    
    height = extractfromstring('h', g)
    height_list.append(height)
    
    taper_length = extractfromstring('tl', g)
    taper_length_list.append(taper_length)
    
    taper_pitch = extractfromstring('tp', g)
    taper_pitch_list.append(taper_pitch)
    
    gap = extractfromstring('g', g)
    gap_list.append(gap)
    
    taper_width = extractfromstring('tw', g)
    taper_width_list.append(taper_width)
    
    waveguide_width = extractfromstring('wgw', g)
    waveguide_width_list.append(waveguide_width)
    
    pitch = extractfromstring('p', g)
    pitch_list.append(pitch)
    
    base_thickness = soi_thickness - etch_depth
    base_min = (-soi_thickness/2)
    base_max = base_min+base_thickness
    base_position = (base_max+base_min)/2
    
    fdtd.gdsimport("C:\\Users\\Lim Yudian\\Documents\\mmi_gratings\\"+g+"_base.GDS", g+"_base", 1, "Si (Silicon) - Palik", -(base_thickness/2), (base_thickness/2)) #
    fdtd.set("name", g+"_base")
    fdtd.set("x", 0.0)
    fdtd.set("y", 0.0)
    fdtd.set("z", base_position)
    
    fdtd.gdsimport("C:\\Users\\Lim Yudian\\Documents\\mmi_gratings\\"+g+".GDS", g, 1, "Si (Silicon) - Palik", -(soi_thickness/2), (soi_thickness/2)) #
    fdtd.set("name", g)
    fdtd.set("x", 0.0)
    fdtd.set("y", 0.0)
    fdtd.set("z", 0.0)
    

    
    fdtd.addfdtd()
    fdtd.set("dimension", 2)
    fdtd.set("x min",-1*((width/2)+(taper_length)+fdtd_margin))
    fdtd.set("x max",((width/2)+(taper_length)+fdtd_margin))
    fdtd.set("y min", -1*((height/2)+fdtd_margin))
    fdtd.set("y max", ((height/2)+fdtd_margin))
    fdtd.set("z min", -(soi_thickness)-fdtd_margin_z)
    fdtd.set("z max", (soi_thickness)+fdtd_margin_z)
    fdtd.set("background material", "SiO2 (Glass) - Palik")
    
    fdtd.addpower()
    fdtd.set("name","E_middle")
    fdtd.set("monitor type",7)
    fdtd.set("x min",-1*((width/2)+(taper_length)))
    fdtd.set("x max",((width/2)+(taper_length)))
    fdtd.set("y min", -1*((height/2)))
    fdtd.set("y max", ((height/2)))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set("z", 0)
    
    fdtd.addpower()
    fdtd.set("name","E_bottom")
    fdtd.set("monitor type",7)
    fdtd.set("x min",-1*((width/2)+(taper_length)))
    fdtd.set("x max",((width/2)+(taper_length)))
    fdtd.set("y min", -1*((height/2)))
    fdtd.set("y max", ((height/2)))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set("z", (-soi_thickness))
    
    fdtd.addpower()
    fdtd.set("name","E_top")
    fdtd.set("monitor type",7)
    fdtd.set("x min",-1*((width/2)+(taper_length)))
    fdtd.set("x max",((width/2)+(taper_length)))
    fdtd.set("y min", -1*((height/2)))
    fdtd.set("y max", ((height/2)))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set("z", (soi_thickness))
    
    fdtd.addpower()
    fdtd.set("name","E_in")
    fdtd.set("monitor type",6)
    fdtd.set("x min",-1*((width/2)+(taper_length)))
    fdtd.set("x max",((width/2)+(taper_length)))
    fdtd.set("y", (gap/2)+(taper_width/2))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set("z", 0)
    
    fdtd.addpower()
    fdtd.set("name","E_out")
    fdtd.set("monitor type",6)
    fdtd.set("x min",-1*((width/2)+(taper_length)))
    fdtd.set("x max",((width/2)+(taper_length)))
    fdtd.set("y", (-gap/2)+(-taper_width/2))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set("z", 0)
    
    fdtd.addindex()
    fdtd.set("name","index_monitor")
    fdtd.set("monitor type",2)  # 2D y-normal
    fdtd.set("x min", -1e-6)
    fdtd.set("x max",1e-6)
    fdtd.set("z min", -(soi_thickness+0.1e-6))
    fdtd.set("z max", (soi_thickness+0.1e-6))
    
    plt.figure(figsize=(6, 4))
    plt.title("pitched mmi")
    plt.show()
    plt.close()
    
    def visualizeindex():
        index = fdtd.getresult("index_monitor","index")
        ix = index['index_x']
        ix = ix[:,0,:,0]
    
        iz = index['index_z']
        iz = iz[:,0,:,0]
        index_abs = np.sqrt(np.abs(iz)**2)
    
        x1 = index["x"]
        x1 = x1[:,0]
        x1 = [i*1000000 for i in x1]
        z1 = index["z"]
        z1 = z1[:,0]
        z1 = [i*1000000 for i in z1]
        
        index_abs = index_abs.transpose()
    
        fig,ax=plt.subplots(1,1)
        cp=ax.contourf(x1,z1,index_abs, 200, zdir='z', offset=-100, cmap='jet')
        clb=fig.colorbar(cp)
        clb.ax.set_title('Index', fontweight="bold")
        for l in clb.ax.yaxis.get_ticklabels():
            l.set_weight("bold")
            l.set_fontsize(12)
        ax.set_xlabel('x-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.set_ylabel('z-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.xaxis.label.set_fontsize(13)
        ax.xaxis.label.set_weight("bold")
        ax.yaxis.label.set_fontsize(13)
        ax.yaxis.label.set_weight("bold")
        ax.tick_params(axis='both', which='major', labelsize=13)
        ax.set_yticklabels(ax.get_yticks(), weight='bold')
        ax.set_xticklabels(ax.get_xticks(), weight='bold')
        ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        plt.title(g+'\n')
        plt.show()
        plt.close()
    
    visualizeindex()

    
    fdtd.addport()
    fdtd.set("name","port 1")
    fdtd.set('x', -1*((width/2)+(taper_pitch/2)+(taper_length)))
    fdtd.set('y min', (gap/2) + (taper_width/2) - (waveguide_width/2))
    fdtd.set('y max', (gap/2) + (taper_width/2) + (waveguide_width/2))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set('injection axis', 'x-axis')
    fdtd.set('direction', 'Forward')
    
    fdtd.addport()
    fdtd.set("name","port 2")
    fdtd.set('x', ((width/2)+(taper_pitch/2)+(taper_length)))
    fdtd.set('y min', (gap/2) + (taper_width/2) - (waveguide_width/2))
    fdtd.set('y max', (gap/2) + (taper_width/2) + (waveguide_width/2))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set('injection axis', 'x-axis')
    fdtd.set('direction', 'Backward')
    
    fdtd.addport()
    fdtd.set("name","port 3")
    fdtd.set('x', -1*((width/2)+(taper_pitch/2)+(taper_length)))
    fdtd.set('y min', (-gap/2) + (-taper_width/2) + (-waveguide_width/2))
    fdtd.set('y max', (-gap/2) + (-taper_width/2) - (-waveguide_width/2))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set('injection axis', 'x-axis')
    fdtd.set('direction', 'Forward')
    
    fdtd.addport()
    fdtd.set("name","port 4")
    fdtd.set('x', ((width/2)+(taper_pitch/2)+(taper_length)))
    fdtd.set('y min', (-gap/2) + (-taper_width/2) + (-waveguide_width/2))
    fdtd.set('y max', (-gap/2) + (-taper_width/2) - (-waveguide_width/2))
    fdtd.set("z min", -(soi_thickness))
    fdtd.set("z max", (soi_thickness))
    fdtd.set('injection axis', 'x-axis')
    fdtd.set('direction', 'Backward')
    
    fdtd.setglobalsource("wavelength start",1500e-9)
    fdtd.setglobalsource("wavelength stop",1600e-9)
    fdtd.setglobalmonitor("frequency points",30)
    
    fdtd.save('C:\\Users\\Lim Yudian\\Documents\\mmi_gratings\\script_run.fsp')
    print("simulating......")
    fdtd.run()
    print("simulation done!")
    
    def getE(port, port_list):
        E = fdtd.getresult("FDTD::ports::"+port,"E")
        y1 = E["y"]
        y1 = y1[:,0]
        y1 = [i*1000000 for i in y1]
        z1 = E["z"]
        z1 = z1[:,0]
        z1 = [i*1000000 for i in z1]
        E1 = E["E"]
        Ex1 = E1[:,:,:,0,0]
        Ey1 = E1[:,:,:,0,1]
        Ez1 = E1[:,:,:,0,2]
        Emag1 = np.sqrt(np.abs(Ex1)**2 + np.abs(Ey1)**2 + np.abs(Ez1)**2)
        Emag1 = Emag1[0,:,:]
        port_list.append(Emag1)
        Emag1 = Emag1.transpose()
        
        fig,ax=plt.subplots(1,1)
        cp=ax.contourf(y1,z1,Emag1, 200, zdir='z', offset=-100, cmap='jet')
        clb=fig.colorbar(cp)
        clb.ax.set_title('Electric Field (eV)', fontweight="bold")
        for l in clb.ax.yaxis.get_ticklabels():
            l.set_weight("bold")
            l.set_fontsize(12)
        ax.set_xlabel('y-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.set_ylabel('z-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.xaxis.label.set_fontsize(13)
        ax.xaxis.label.set_weight("bold")
        ax.yaxis.label.set_fontsize(13)
        ax.yaxis.label.set_weight("bold")
        ax.tick_params(axis='both', which='major', labelsize=13)
        ax.set_yticklabels(ax.get_yticks(), weight='bold')
        ax.set_xticklabels(ax.get_xticks(), weight='bold')
        ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        plt.title(port)
        plt.show()
        plt.close()
    
    getE('port 1', port1_list)
    getE('port 2', port2_list)
    getE('port 3', port3_list)
    getE('port 4', port4_list)
    
    def getT(port, port_list):
        T = fdtd.getresult("FDTD::ports::"+port,"T")
        wavelength = T['lambda']
        T_abs = T['T']
        port_list.append(T_abs)
        plt.plot(wavelength, T_abs)
        plt.title(g+port+" T")
        plt.show()
        plt.close()
    
    getT('port 1', port1T_list)
    getT('port 2', port2T_list)
    getT('port 3', port3T_list)
    getT('port 4', port4T_list)
    
    def visualizeExy(E_monitor):
    
        E = fdtd.getresult(E_monitor,"E")
        E2 = E["E"]
        Ex1 = E2[:,:,:,0,0]
        Ey1 = E2[:,:,:,0,1]
        Ez1 = E2[:,:,:,0,2]
        Emag1 = np.sqrt(np.abs(Ex1)**2 + np.abs(Ey1)**2 + np.abs(Ez1)**2)
        Emag1 = Emag1[:,:,0]
        x1 = E["x"]
        x1 = x1[:,0]
        x1 = [i*1000000 for i in x1]
        y1 = E["y"]
        y1 = y1[:,0]
        y1 = [j*1000000 for j in y1]
        
        Emag1 = Emag1.transpose()
    
        fig,ax=plt.subplots(1,1)
        cp=ax.contourf(x1,y1,Emag1, 200, zdir='z', offset=-100, cmap='jet')
        clb=fig.colorbar(cp)
        clb.ax.set_title('Electric Field (eV)', fontweight="bold")
        for l in clb.ax.yaxis.get_ticklabels():
            l.set_weight("bold")
            l.set_fontsize(12)
        ax.set_xlabel('x-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.set_ylabel('y-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.xaxis.label.set_fontsize(13)
        ax.xaxis.label.set_weight("bold")
        ax.yaxis.label.set_fontsize(13)
        ax.yaxis.label.set_weight("bold")
        ax.tick_params(axis='both', which='major', labelsize=13)
        ax.set_yticklabels(ax.get_yticks(), weight='bold')
        ax.set_xticklabels(ax.get_xticks(), weight='bold')
        ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        plt.title(E_monitor)
        plt.show()
        plt.close()
    visualizeExy("E_bottom")
    visualizeExy("E_middle")
    visualizeExy("E_top")
    
    def visualizeExz(E_monitor):
        E = fdtd.getresult(E_monitor,"E")
        E2 = E["E"]
        Ex1 = E2[:,:,:,0,0]
        Ey1 = E2[:,:,:,0,1]
        Ez1 = E2[:,:,:,0,2]
        Emag1 = np.sqrt(np.abs(Ex1)**2 + np.abs(Ey1)**2 + np.abs(Ez1)**2)
        Emag1 = Emag1[:,0,:]
        x1 = E["x"]
        x1 = x1[:,0]
        x1 = [i*1000000 for i in x1]
        z1 = E["z"]
        z1 = z1[:,0]
        z1 = [j*1000000 for j in z1]
        
        Emag1 = Emag1.transpose()
    
        fig,ax=plt.subplots(1,1)
        cp=ax.contourf(x1,z1,Emag1, 200, zdir='z', offset=-100, cmap='jet')
        clb=fig.colorbar(cp)
        clb.ax.set_title('Electric Field (eV)', fontweight="bold")
        for l in clb.ax.yaxis.get_ticklabels():
            l.set_weight("bold")
            l.set_fontsize(12)
        ax.set_xlabel('x-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.set_ylabel('y-position (µm)', fontsize=13, fontweight="bold", labelpad=1)
        ax.xaxis.label.set_fontsize(13)
        ax.xaxis.label.set_weight("bold")
        ax.yaxis.label.set_fontsize(13)
        ax.yaxis.label.set_weight("bold")
        ax.tick_params(axis='both', which='major', labelsize=13)
        ax.set_yticklabels(ax.get_yticks(), weight='bold')
        ax.set_xticklabels(ax.get_xticks(), weight='bold')
        ax.xaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        ax.yaxis.set_major_formatter(StrMethodFormatter('{x:,.1f}'))
        plt.title(E_monitor)
        plt.show()
        plt.close()
    visualizeExz("E_in")
    visualizeExz("E_out")
    
    plt.figure(figsize=(6, 4))
    plt.title("base mmi")
    plt.show()
    plt.close()
    
    fdtd.switchtolayout()
    fdtd.select(g)
    fdtd.delete()   
    fdtd.select(g+"_base")
    fdtd.delete() 
    
    fdtd.gdsimport("C:\\Users\\Lim Yudian\\Documents\\mmi_gratings\\"+g+"_base.GDS", g+"_base", 1, "Si (Silicon) - Palik", -(soi_thickness/2), (soi_thickness/2)) #
    fdtd.set("name", g+"_base")
    fdtd.set("x", 0.0)
    fdtd.set("y", 0.0)
    fdtd.set("z", 0.0)
    
    visualizeindex()
    
    fdtd.save('C:\\Users\\Lim Yudian\\Documents\\mmi_gratings\\script_run.fsp')
    print("simulating......")
    fdtd.run()
    print("simulation done!")
    
    getE('port 1', port1base_list)
    getE('port 2', port2base_list)
    getE('port 3', port3base_list)
    getE('port 4', port4base_list)
    
    getT('port 1', port1Tbase_list)
    getT('port 2', port2Tbase_list)
    getT('port 3', port3Tbase_list)
    getT('port 4', port4Tbase_list)
    
    visualizeExy("E_bottom")
    visualizeExy("E_middle")
    visualizeExy("E_top")
    
    visualizeExz("E_in")
    visualizeExz("E_out")
    
    
    
else:
    print("Base GDS is missing for "+g)

df_results = pd.DataFrame()
df_results['port1_list'] = port1_list
df_results['port2_list'] = port2_list
df_results['port3_list'] = port3_list
df_results['port4_list'] = port4_list
df_results['port1T_list'] = port1T_list
df_results['port2T_list'] = port2T_list
df_results['port3T_list'] = port3T_list
df_results['port4T_list'] = port4T_list
df_results['port1base_list'] = port1base_list
df_results['port2base_list'] = port2base_list
df_results['port3base_list'] = port3base_list
df_results['port4base_list'] = port4base_list
df_results['port1Tbase_list'] = port1Tbase_list
df_results['port2Tbase_list'] = port2Tbase_list
df_results['port3Tbase_list'] = port3Tbase_list
df_results['port4Tbase_list'] = port4Tbase_list
df_results['width_list'] = width_list
df_results['height_list'] = height_list
df_results['taper_length_list'] = taper_length_list
df_results['taper_pitch_list'] = taper_pitch_list
df_results['gap_list'] = gap_list
df_results['taper_width_list'] = taper_width_list
df_results['waveguide_width_list'] = waveguide_width_list
df_results['pitch_list'] = pitch_list


