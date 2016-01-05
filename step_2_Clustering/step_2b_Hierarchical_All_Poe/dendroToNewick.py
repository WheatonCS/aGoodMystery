# Run with:  Python 2.7.10 |Anaconda 2.3.0 (x86_64)
# (yeah, that's important :)

"""
make DTM of directory of texts and
cluster (sklearn, scipy) and plot dendrograms in two ways:
  (1) hierarchical dendrogram: matplotlib.pyplot  
  (2) Save the linkage matrix to a scipy tree
        Convert the scipy tree to an ETE tree
        Convert the ETE tree to a Newick string and write it to a file
           (Environment for (phylogenetic) Tree Exploration, http://etetoolkit.org/)
           
 scottKleinman, mleblanc
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances 
from scipy.spatial.distance import pdist 
from scipy.cluster.hierarchy import linkage, average, weighted, single, complete, dendrogram, to_tree
import matplotlib.pyplot as plt
from ete2 import Tree, TreeStyle, NodeStyle

import os
import glob

### Configuration ###
# Set dendrogram orientation
orientation = "top" # Alternatives: "right", "bottom", left"

# Set output path for Newick string
output_path = ""

# Add the source files to this list
#filenames = ["Cooper_LastMohicans_1.txt", "Hawthorne_TwiceToldTales_1.txt", "Melville_MobyDick_1.txt"]

filenames = glob.glob("PoeTexts/*.txt")
# print (filenames)


# Add the labels to be displayed for each file to this list
#labels = ["Cooper", "Hawthorne", "Melville"]

labels = []
for nextFile in filenames:
    # texts/Cooper_LastMohicans_1.txt
    start = nextFile.index('/')
    end   = nextFile.index('.txt')
    newLabel = nextFile[start+1:end]
    #print(newLabel)
    #junk = input("pause")
    labels.append(newLabel)
### End Configuration ###

#print(labels)
#junk = input("pause")
    
# Load the files and make a sparse Document-Term-Matrix (DTM)
vectorizer = CountVectorizer(input='filename')
DocTermSparseMatrix = vectorizer.fit_transform(filenames)
dtm = DocTermSparseMatrix.toarray()

#print (dtm[1:5,:])

## Create distance matrix
Y = euclidean_distances(dtm)

# Or, if you want to supply the metric as a variable:
#metric = "euclidean" # For alternatives, see http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.spatial.distance.pdist.html
#Y = pdist(dtm, metric)

## Create linkage matrix. Choose your method (see imports above):
Z = average(Y)
#Z = single(Y)
#Z = weighted(Y)
#Z = complete(Y)

# Or, if you want to supply the method as a variable:        
#linkage = "average"
#Z = hierarchy.linkage(Y, method=linkage)

# Adjust dendrogram labels based on configuration
if orientation == "top":
    LEAF_ROTATION_DEGREE = 90
else:
    LEAF_ROTATION_DEGREE = 0

# Create the dendrogram
dendrogram(Z, orientation=orientation, leaf_rotation=LEAF_ROTATION_DEGREE, labels=labels)

# (1) hierarchical dendrogram: sklearn-learn 
# Plot the hierarchical dendrogram if desired
#plt.tight_layout()  # fixes margins
#plt.show()


#  (2) Newick circular format: ETE (Environment for (phylogenetic) Tree Exploration)

# Save the linkage matrix to a scipy tree
T = to_tree(Z)

# Convert the scipy tree to an ETE tree
root = Tree()
root.dist = 0
root.name = "root"
item2node = {T: root}

to_visit = [T]
while to_visit:
    node = to_visit.pop()
    cl_dist = node.dist /2.0
    for ch_node in [node.left, node.right]:
        if ch_node:
            ch = Tree()
            ch.dist = cl_dist
            ch.name = str(ch_node.id)
            item2node[node].add_child(ch)
            item2node[ch_node] = ch
            to_visit.append(ch_node)

# This is the ETE tree structure
tree = root

# Convert the ETE tree to a Newick string and write it to a file
newick = tree.write()
#output_path = "mytree.png"
#f = open(output_path, 'w')
#f.write(newick)
#f.close()

## Bonus ETE dendrogram plotting

# Configure output path for image
#ete_output_path="eteTree.png"
width = 600 # For other output args, see http://etetoolkit.org/docs/latest/tutorial/tutorial_drawing.html#rendering-trees-as-images

# Configure tree styles
ts = TreeStyle()
ts.show_leaf_name = True
ts.show_branch_length = True
ts.show_scale = False
ts.scale =  None

ts.mode = "c" # draw tree in circular style
ts.arc_start = 0
ts.arc_span = 360

if orientation == "top":
    ts.rotation = 90
    ts.branch_vertical_margin = 10 # 10 pixels between adjacent branches

# Remove the default small red spheres for each node
nstyle = NodeStyle()
nstyle["size"] = 0
for leaf in tree:
    k = leaf.name
    k = int(k)
    leaf.name = labels[k]

# Apply node styles to nodes
for n in tree.traverse():
   n.set_style(nstyle)

# Plot the tree
tree.show(tree_style=ts)

# Or save it
ete_output_path = "eteTree.png"
#tree.render(ete_output_path, w=width, units="px", tree_style=ts)
