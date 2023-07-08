import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Function to plot the degree distribution PDF on a log-log scale
def plot_degree_distribution_pdf(graph_type, graph, title, ax):
    degrees = [degree for node, degree in graph.degree()]
    degree_count = np.bincount(degrees)
    pdf = degree_count / len(degrees)

    ax.loglog(range(len(pdf)), pdf, '.', alpha=0.7, label=graph_type)
    ax.set_title(title)
    ax.set_xlabel('Degree (log scale)')
    ax.set_ylabel('Probability Density (log scale)')

# Generate SF graphs
n = 500  # Number of nodes
m = 4  # Number of edges to attach from a new node to existing nodes
num_graphs = 1000  # Number of SF graphs to generate

batch_size = 100  # Number of graphs to generate in each batch
num_batches = num_graphs // batch_size

sf_graphs = []
for i in range(num_batches):
    print(f"Generating batch {i+1}/{num_batches}...")
    batch_graphs = [nx.barabasi_albert_graph(n, m) for _ in range(batch_size)]
    sf_graphs.extend(batch_graphs)

# Plotting the degree distribution PDFs for SF graphs with different parameters
fig, ax = plt.subplots()

for i, graph in enumerate(sf_graphs):
    graph_type = f"SF (Graph {i+1})"
    plot_degree_distribution_pdf(graph_type, graph, f"SF Degree Distribution PDF (Graph {i+1})", ax)

plt.legend()
plt.show()


# Function to calculate the average degree of a graph
def calculate_average_degree(graph):
    degrees = [degree for node, degree in graph.degree()]
    return np.mean(degrees)

# Generate SF graphs and calculate average degree for each network size
start_size = 100  # Starting network size
end_size = 1000  # Ending network size
step_size = 100  # Step size for increasing network size
num_graphs = 10  # Number of SF graphs to generate for each size
m = 4  # Number of edges to attach from a new node to existing nodes

network_sizes = range(start_size, end_size + step_size, step_size)
average_degrees = []

for size in network_sizes:
    sf_graphs = [nx.barabasi_albert_graph(size, m) for _ in range(num_graphs)]
    average_degree = np.mean([calculate_average_degree(graph) for graph in sf_graphs])
    average_degrees.append(average_degree)

# Plotting the average degree as a function of network size
plt.plot(network_sizes, average_degrees, 'bo-')
plt.title("Average Degree vs. Network Size")
plt.xlabel("Network Size")
plt.ylabel("Average Degree")
plt.show()

