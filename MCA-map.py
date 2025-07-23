import matplotlib.pyplot as plt



# Provided MCA coordinates and cluster colors
data = [
    {"keyword": "Fuzzy Logic", "x": 0.5, "y": 0.5, "color": "red", "cluster": "Fuzzy MCDM"},
    {"keyword": "TOPSIS", "x": 0.7, "y": 1.0, "color": "red", "cluster": "Fuzzy MCDM"},
    {"keyword": "AHP", "x": 0.3, "y": 0.0, "color": "red", "cluster": "Fuzzy MCDM"},
    {"keyword": "Corporate Governance", "x": 1.5, "y": 1.5, "color": "blue", "cluster": "Governance"},
    {"keyword": "Regulatory Compliance", "x": 2.0, "y": 2.0, "color": "green", "cluster": "Compliance"},
    {"keyword": "Policy-Making", "x": 1.7, "y": 1.2, "color": "blue", "cluster": "Governance"},
    {"keyword": "Risk Assessment", "x": 2.5, "y": 2.5, "color": "green", "cluster": "Compliance"},
    {"keyword": "Stakeholder Engagement", "x": 2.2, "y": 1.8, "color": "blue", "cluster": "Governance"},
    {"keyword": "Audit Systems", "x": 2.8, "y": 2.8, "color": "green", "cluster": "Compliance"},
    {"keyword": "Decision Optimization", "x": 3.5, "y": 0.5, "color": "yellow", "cluster": "Optimization"}
]

# Create scatter plot
plt.figure(figsize=(8, 6))
for point in data:
    plt.scatter(point["x"], point["y"], c=point["color"], s=50, label=point["cluster"] if point["keyword"] == "Fuzzy Logic" or point["keyword"] == "Corporate Governance" or point["keyword"] == "Regulatory Compliance" or point["keyword"] == "Decision Optimization" else "")
    plt.text(point["x"] + 0.05, point["y"], point["keyword"], fontsize=10, fontfamily="Arial")

# Customize axes and grid
plt.xlabel("Frequency", fontsize=12, fontfamily="Arial")
plt.ylabel("Cluster Separation", fontsize=12, fontfamily="Arial")
plt.grid(True, linestyle="--", alpha=0.7)
plt.xticks(fontsize=10, fontfamily="Arial")
plt.yticks(fontsize=10, fontfamily="Arial")

# Handle legend to avoid duplicate entries
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys(), fontsize=10)

# Save as PNG
plt.savefig("MCA_Conceptual_Structure_Map.png", dpi=300, bbox_inches="tight")
# Save as SVG
plt.savefig("MCA_Conceptual_Structure_Map.svg", format="svg", bbox_inches="tight")

plt.close()
