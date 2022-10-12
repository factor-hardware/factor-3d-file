import sys
from tkinter.messagebox import NO
from converter.mesh_converter import mesh_converter
import igl
import scipy as sp
import numpy as np

class shape_diameter_compute():

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.normals = None
        self.shape_diameter = None

    def generate_normals(self, print_normals=False):
        self.normals = igl.per_vertex_normals(self.vertices, self.faces)
        if print_normals:
            print(self.normals)
    
    def generate_shape_diameter(self, num_samples, print_shape_diameter=False):
        if self.vertices.any() and self.faces.any() and self.normals.any():
            self.shape_diameter = igl.shape_diameter_function(self.vertices, self.faces, self.vertices, self.normals, num_samples)
            if print_shape_diameter:
                print(len(self.shape_diameter))
                print(self.shape_diameter)
        elif print_shape_diameter:
            print('please compute vertices, faces, and normals before executing this function')
    
    def get_shape_diameter(self):
        return self.shape_diameter

MESH_FILE_INPUT_PATH = 1
NUM_SAMPLES = 100
if __name__ == '__main__':
    fmc = mesh_converter(sys.argv[MESH_FILE_INPUT_PATH])
    fmc.ingest_3d_file()
    mesh = fmc.get_triangles()
    if mesh:
        vertices, faces = mesh
        sdc = shape_diameter_compute(vertices, faces['triangle'])
        print('generating normals')
        sdc.generate_normals()
        print('calling shape diameter function')
        sdc.generate_shape_diameter(NUM_SAMPLES, True)