import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
import math
from collections import defaultdict


# Function to plot the degree distribution PDF
def plot_degree_distribution_pdf(graph_type, degrees, title):
    degree_count = np.bincount(degrees)
    pdf = degree_count / len(degrees)

    plt.bar(range(len(pdf)), pdf, width=0.8, color='b')
    plt.title(title)
    plt.xlabel('Degree')
    plt.ylabel('Probability Density')
    plt.xticks(np.arange(0, max(degrees)+1, 1))
    plt.xlim([-0.5, max(degrees)+0.5])
    plt.show()

# Random Scale-Free Recursive Graph (RSRG)
def plot_rsr_graph():
    graph = nx.barabasi_albert_graph(100, 3, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='RSRG')

# Random Scale-Free Recursive Bipartite Graph (RSRBG)
def plot_rsr_bipartite_graph():
    graph = nx.bipartite.random_graph(10, 5, 0.5, seed=42)
    projection = nx.bipartite.projected_graph(graph, list(range(10)))
    degrees = [degree for _, degree in projection.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='RSRBG')

# Watts-Strogatz (WS)
def plot_ws_graph():
    graph = nx.watts_strogatz_graph(100, 4, 0.3, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='WS')

# Scale-Free (SF)
def plot_sf_graph():
    graph = nx.scale_free_graph(100, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='SF')

# Erdos-Renyi (ER)
def plot_er_graph():
    graph = nx.erdos_renyi_graph(100, 0.15, seed=42)
    degrees = [degree for _, degree in graph.degree()]
    degree_hist = np.histogram(degrees, bins=range(max(degrees) + 2))[0]
    degree_pdf = degree_hist / sum(degree_hist)
    plt.plot(range(len(degree_pdf)), degree_pdf, label='ER')

# Plotting all graphs
plot_rsr_graph()
plot_rsr_bipartite_graph()
plot_ws_graph()
plot_sf_graph()
plot_er_graph()

# Setting plot properties
plt.xlabel('Degree')
plt.ylabel('Probability Density')
plt.title('Degree Distribution PDF')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()




# Random Scale-Free Recursive Graph (RSRG)
def plot_rsr_graph():
    graph = nx.barabasi_albert_graph(100, 3, seed=42)
    eigenvalues = np.linalg.eigvals(nx.to_numpy_array(graph))
    eigenvalue_hist = np.histogram(eigenvalues, bins=30)[0]
    eigenvalue_pdf = eigenvalue_hist / sum(eigenvalue_hist)
    plt.plot(range(len(eigenvalue_pdf)), eigenvalue_pdf, label='RSRG')

# Random Scale-Free Recursive Bipartite Graph (RSRBG)
def plot_rsr_bipartite_graph():
    graph = nx.bipartite.random_graph(10, 5, 0.5, seed=42)
    eigenvalues = np.linalg.eigvals(nx.to_numpy_array(graph))
    eigenvalue_hist = np.histogram(eigenvalues, bins=30)[0]
    eigenvalue_pdf = eigenvalue_hist / sum(eigenvalue_hist)
    plt.plot(range(len(eigenvalue_pdf)), eigenvalue_pdf, label='RSRBG')

# Watts-Strogatz (WS)
def plot_ws_graph():
    graph = nx.watts_strogatz_graph(100, 4, 0.3, seed=42)
    eigenvalues = np.linalg.eigvals(nx.to_numpy_array(graph))
    eigenvalue_hist = np.histogram(eigenvalues, bins=30)[0]
    eigenvalue_pdf = eigenvalue_hist / sum(eigenvalue_hist)
    plt.plot(range(len(eigenvalue_pdf)), eigenvalue_pdf, label='WS')

# Scale-Free (SF)
def plot_sf_graph():
    graph = nx.scale_free_graph(100, seed=42)
    eigenvalues = np.linalg.eigvals(nx.to_numpy_array(graph))
    eigenvalue_hist = np.histogram(eigenvalues, bins=30)[0]
    eigenvalue_pdf = eigenvalue_hist / sum(eigenvalue_hist)
    plt.plot(range(len(eigenvalue_pdf)), eigenvalue_pdf, label='SF')

# Erdos-Renyi (ER)
def plot_er_graph():
    graph = nx.erdos_renyi_graph(100, 0.15, seed=42)
    eigenvalues = np.linalg.eigvals(nx.to_numpy_array(graph))
    eigenvalue_hist = np.histogram(eigenvalues, bins=30)[0]
    eigenvalue_pdf = eigenvalue_hist / sum(eigenvalue_hist)
    plt.plot(range(len(eigenvalue_pdf)), eigenvalue_pdf, label='ER')

# Plotting all graphs
plot_rsr_graph()
plot_rsr_bipartite_graph()
plot_ws_graph()
plot_sf_graph()
plot_er_graph()

# Setting plot properties
plt.xlabel('Eigenvalue Index')
plt.ylabel('Probability Density')
plt.title('Eigenvalue Distribution PDF')
plt.legend()
plt.grid(True)

# Display the plot
plt.show()