import sys
import vtk
import os
import platform
import pyvista as pv
from pyvirtualdisplay import Display

#def bubble_wrap_calc(bubble_wrap_size, mesh, iter_num):
#    is_equal = False
#    for i in range(1, iter_num):
#        # perform calculations with bubble_wrap and mesh
#        # grab results from FEA analsys
#        equal_forces = result.fea_analysis_force
#        if abs(equal_forces) < 1:
#            is_equal = True
#            break
#        
#    return is_equal
class stl_visualizer():
    
    def __init__(self):
        pass

    def visualize_vtk(self, vtk_mesh):
        display = Display(visible=0, size=(1280, 1024))
        display.start()
        plotter = pv.Plotter()
        plotter.add_mesh(vtk_mesh, show_edges=True)
        plotter.show(window_size=[512, 384], cpos="iso")
        display.stop()

    def create_vtk(self, stl_mesh_path : str):
        out_vtk = None
        if '.stl' in stl_mesh_path:
            render_vtk = vtk.vtkSTLReader()
            render_vtk.SetFileName(stl_mesh_path)
            render_vtk.Update()
            out_vtk = render_vtk.GetOutput()
        return out_vtk

def setup_for_platform():
    if platform.system() == 'Darwin':
        os.environ["PATH"] += os.pathsep + '/opt/X11/bin'

if __name__ == "__main__":
    stl_mesh_path = str(sys.argv[1])
    setup_for_platform()

    visualizer = stl_visualizer()
    vtk_mesh = visualizer.create_vtk(stl_mesh_path)
    if vtk_mesh:
        print('visualizing')
        visualizer.visualize_vtk(vtk_mesh)
    else:
        print('file invalid, visualization failed')
