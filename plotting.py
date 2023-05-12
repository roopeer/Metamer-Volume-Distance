# -*- coding: utf-8 -*-
"""plotting

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CJwYKcyEuuZNCKdJUMPoYD2lpMBR7woF
"""

import numpy as np
import plotly.offline as py
import plotly.graph_objs as go

def mesh_from_hull(hull):
	vertices = hull.points
	faces = hull.simplices
	mesh = \
		go.Mesh3d(
		   x=np.array(vertices)[:,0],
		   y=np.array(vertices)[:,1],
		   z=np.array(vertices)[:,2],
		   i=np.array(faces)[:,0],
		   j=np.array(faces)[:,1],
		   k=np.array(faces)[:,2],
		   opacity=0.5)
	return mesh

def scatter_from_points(point):
  pt = go.Scatter3d(x=np.array(point[0]), y=np.array(point[1]), z=np.array(point[2]))
  return pt

def plot_convex_hulls(hulls, points, filename):
  layout = go.Layout()
  meshes = [mesh_from_hull(h) for h in hulls]
  pts = [scatter_from_points(point) for point in points]
  py.plot(go.Figure(data=meshes + pts, layout=layout), filename=filename)