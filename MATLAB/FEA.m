%% MAE 586 Project 
clear all 
clc

%% user inputs and material properties (some metal)
E = 2.4e9; % Young's modulus in Pa 
nu = 0.37; % Poisson's ratio 
density = 2.12; % in kg/m^3
units = 'mm';


%%
tic
smodel = createpde('structural','static-solid'); 
importGeometry(smodel,'../3d_files/upper-arm.STL'); % had to change part b/c first part had too many faces (over 40-ish) and I waited over 10 minutes for the mesh to generate and it still wasn't finished)


figure(1)
pdegplot(smodel, 'FaceLabels', 'on', 'FaceAlpha', 0.5); % add timer

figure(2)
msh = generateMesh(smodel); 
pdeplot3D(smodel)


structuralProperties(smodel, 'YoungsModulus', E, 'PoissonsRatio', nu)


%%
V = volume(msh);
% A = surfaceArea(smodel)
[V,VE] = volume(msh);

mass = V*density; 

%% 
x = 0.185;
new_mass = mass;
num_layers = []; 


% new_mass = new_mass+(mass*percent_change);

while new_mass >= 0
    percent_change = -0.31356*x - 0.10156;
    new_mass = mass+(mass*percent_change);
    x = x + 0.185;

end 

num_layers = x/0.185; 

toc
