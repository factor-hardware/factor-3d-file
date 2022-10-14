import sys
import meshio

class mesh_creator():

    def __init__(self):
        pass

    def create_mesh(self, vertices, faces, colors):
        return meshio.Mesh(
            vertices,
            faces,
            cell_data = {
                "a": [colors]
            }
        )

class mesh_converter():

    def __init__(self, mesh_path : str):
        self.mesh_path = mesh_path
        self.mesh_data = None
        self.converted_mesh_data = None

    def ingest_3d_file(self, printData=False):
        try:
            self.mesh_data = meshio.read(self.mesh_path)
            if printData:
                print(self.mesh_data)
        except IOError:
            print('read failed')
    
    def write_to_disk(self, output_mesh_name : str):
        if self.mesh_data:
            try:
                meshio.write(output_mesh_name, self.mesh_data)
            except IOError:
                print('mesh write failed')
    
    def get_triangles(self):
        triangles = None
        if self.mesh_data:
            triangles = (self.mesh_data.points, self.mesh_data.cells_dict)
        return triangles
    
    def set_mesh(self, mesh):
        self.mesh_data = mesh


MESH_FILE_INPUT_PATH = 1
MESH_FILE_OUTPUT_PATH = 2
if __name__ == '__main__':
    fmc = mesh_converter(sys.argv[MESH_FILE_INPUT_PATH])
    fmc.ingest_3d_file(True)
    fmc.write_to_disk(sys.argv[MESH_FILE_OUTPUT_PATH])