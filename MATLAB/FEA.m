%% MAE 586 Project 

clear all 
clc

tic
%% user inputs and material properties 

dimension_units = 'mm';
hardness = 217; % brinell hardess in kgf/mm^2 
density = 8.03; % in grams/cm^3 (grams/cc)
density_mm = density/1000; % in grams/mm^3
g = 9810; % acceleration due to gravity in mm/s^2
height = 50; % in feet
height_mm = height*304.8; % in mm

%% creating FE mesh

smodel = createpde('structural','static-solid'); 
importGeometry(smodel,'../3d_files/upper-arm.STL'); 

figure(1)
pdegplot(smodel, 'FaceLabels', 'on', 'FaceAlpha', 0.5); % add timer

figure(2)
msh = generateMesh(smodel); 
pdeplot3D(smodel)

%% Volume, surface area, and mass calculations 

V = volume(msh); % in mm^3
[V,VE] = volume(msh);
[X,Y,Z] = meshgrid(msh);
x = X.Nodes(1,:)';
y = Y.Nodes(2,:)';
z = Z.Nodes(3,:)';
shp = alphaShape(x,y,z); 
A = surfaceArea(shp);

mass = V*density_mm; % units in grams

%% initial constants

thickness = 0.1875; % thickness of 1 layer of bubble wrap in inches
acceleration_force = mass*g*height_mm; % in (grams*mm^2)/s^2)
new_acceleration = acceleration_force;
hardness_adjusted = (hardness*9.806650)*A; % kgf/mm^2 to N/mm^2 = (grams*mm/s^2)/mm^2)*mm^2 = (grams*mm^2/s^2)


%% finding thickness and number of layers needed for the accerlation force to become less than the hardness of the material

while new_acceleration >= hardness_adjusted
    percent_change = (-31.356*thickness - 10.156)/100;
    new_acceleration = new_acceleration+(new_acceleration*percent_change);
    thickness = thickness + 0.1875; % in inches

end 

num_layers = ceil(thickness/0.1875)
final_thickness = thickness

toc



