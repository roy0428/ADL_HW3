import matplotlib.pyplot as plt

def main():
    completed_steps = [148, 296, 444, 580]
    mean_perplexity_list = [4.1553508992195125, 3.8066051182746885, 3.8777953686714173, 3.8654263515472413]

    plt.subplot(111)
    plt.plot(completed_steps, mean_perplexity_list,label='Mean_Perplexity')
    plt.xlabel("Completed Steps")
    plt.ylabel("Mean_Perplexity")
    plt.title("Mean_Perplexity Curve")
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()