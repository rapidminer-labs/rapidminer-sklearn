from src.mixture import GaussianMixture
import seaborn as sns


def test():
    """"
        TODO: Move to proper testing
    """
    iris = sns.load_dataset('iris')
    iris = iris.drop("species", axis=1)
    gmm, bic = GaussianMixture.rm_train(iris, params={})
    result = GaussianMixture.rm_apply(iris, gmm)

    print(result)


if __name__ == "__main__":
    test()
