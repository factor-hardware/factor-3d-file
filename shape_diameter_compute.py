import sys
from converter.mesh_converter import mesh_converter, mesh_creator
import igl
import scipy as sp
import numpy as np

class shape_diameter_compute():

    def __init__(self, vertices, faces):
        self.vertices = vertices
        self.faces = faces
        self.normals = None
        self.bounding_box_diagonal = None
        self.shape_diameter = None

    def generate_normals(self, print_normals=False):
        self.normals = igl.per_vertex_normals(self.vertices, self.faces)
        if print_normals:
            print(len(self.normals))
        assert(self.normals is not None)
    
    def set_bounding_box_diagonal(self, print_bounding_box=False):
        if self.vertices.any():
            self.bounding_box_diagonal = igl.bounding_box_diagonal(self.vertices)
            if print_bounding_box:
                print(self.bounding_box_diagonal)
        assert(self.bounding_box_diagonal is not None)

    def generate_shape_diameter(self, num_samples, normalize=True, print_shape_diameter=False):
        if self.vertices.any() and self.faces.any() and self.normals.any():
            self.shape_diameter = igl.shape_diameter_function(self.vertices, self.faces, self.vertices, self.normals, num_samples)
            if normalize and self.bounding_box_diagonal:
                self.shape_diameter /= self.bounding_box_diagonal
            if print_shape_diameter:
                print(len(self.shape_diameter))
        elif print_shape_diameter:
            print('please compute vertices, faces, and normals before executing this function')
        assert(self.shape_diameter is not None)
    
    def get_shape_diameter(self):
        return self.shape_diameter

MESH_FILE_INPUT_PATH = 1
NUM_SAMPLES = 2
DEFAULT_NUM_SAMPLES = 100
if __name__ == '__main__':
    mconv = mesh_converter(sys.argv[MESH_FILE_INPUT_PATH])
    mconv.ingest_3d_file()
    mesh = mconv.get_triangles()
    if mesh:
        vertices, faces = mesh
        sdc = shape_diameter_compute(vertices, faces['triangle'])
        num_samples = int(sys.argv[NUM_SAMPLES]) if len(sys.argv) == 3 else DEFAULT_NUM_SAMPLES
        print('generating normals')
        sdc.generate_normals(True)
        print('set bounding box')
        sdc.set_bounding_box_diagonal(True)
        print('calling shape diameter function')
        sdc.generate_shape_diameter(num_samples, print_shape_diameter=True)
        #mcreator = mesh_creator()
        #mconv.set_mesh(mcreator.create_mesh(vertices, faces, sdc.normals, sdc.shape_diameter))
        #mconv.write_to_disk("newMesh.vtk")