import sys
import meshio

class fea_mesh_converter():

    def __init__(self, mesh_path : str):
        self.mesh_path = mesh_path
        self.mesh_data = None
        self.converted_mesh_data = None
        print(self.mesh_path)

    def ingest_3d_file(self):
        try:
            self.mesh_data = meshio.read(self.mesh_path)
            print(self.mesh_data)
        except IOError:
            print('read failed')
    
    def write_to_disk(self, output_mesh_name : str):
        if self.mesh_data:
            try:
                meshio.write(output_mesh_name, self.mesh_data)
            except IOError:
                print('mesh write failed')


MESH_FILE_PATH = 1
if __name__ == '__main__':
    fmc = fea_mesh_converter(sys.argv[MESH_FILE_PATH])
    fmc.ingest_3d_file()
    fmc.write_to_disk('helmet.msh')