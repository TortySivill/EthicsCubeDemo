
import pathlib
import numpy as np
import plotly.graph_objects as go



def makeMesh(i,j,k, c_i):
  colors = []
  # Example viewing options here demonstrated with colours
  colors.append(['red', 'orange', 'yellow', 'pink', 'green', 'purple', 'blue'])
  colors.append(['orange', 'pink', 'blue', 'green', 'yellow', 'purple', 'red'])
  colors.append(["red", "red", "red", "red", "red", "red", "red"])
  x_cats = ['w','x','y','z']
  mesh1 = go.Mesh3d(
        # 8 vertices of a cube
        x=[i, i, i+1, i+1, i, i, i+1, i+1],
        y=[j, j+1, j+1, j, j, j+1, j+1, j],
        z=[k, k, k, k, k+1, k+1, k+1, k+1],
        color = colors[c_i][k], 
        #Tessaletion options i,j,k
        i= [7, 0, 0, 0, 4, 4, 6, 1, 4, 0, 3, 6],
        j= [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
        k= [0, 7, 2, 3, 6, 7, 1, 6, 5, 5, 7, 2],
        name='y',
        #showscale=True
    )

  return mesh1

def makeMeshes(option):
  if option == "main":
   c_i = 0
  elif option == "view1":
   c_i = 1
  else:
   c_i = 2
  meshes = []
  for i in range(0,3):
    for j in range(0,6):
      for k in range(0,6):
        #Example missing pieces 
        if (i == 0 or i == 3 and j == 0 or j == 2) and k == 0:
          continue
        elif (i == 1 or i == 2 and j == 1) and k == 1:
          continue
        elif (i == 0) and k == 2:
          continue
        elif (i == 3 or i == 2 and j == 5 or  j == 6) and k == 3:
          continue
        elif (i == 0 or i == 3 and  j == 1 or j == 3 or j == 4) and k == 4:
          continue
        elif (i == 1 or i == 2 and j == 1) and k == 5:
          continue
        else:
          meshes.append(makeMesh(i,j,k, c_i))
  
  return meshes 

def create_mesh_data(option):
	data = makeMeshes(option)
	data[0]["name"] = option
	return data

def toggle_mesh_data(hide_values):
  data = makeToggleMeshes(hide_values)
  data[0]["name"] = "main" #TODO make this relative to view
  return data


