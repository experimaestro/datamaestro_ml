from datamaestro.data import Generic
from datamaestro.data.csv import Matrix
from datamaestro.definitions import Dataset
from datamaestro.download.single import DownloadFile

@DownloadFile("data", url="https://raw.githubusercontent.com/scikit-learn/scikit-learn/master/sklearn/datasets/data/boston_house_prices.csv")
@Dataset(Generic)
def boston(data):
  """Boston Housing dataset
  
  This dataset contains information collected by the U.S Census Service
  concerning housing in the area of Boston Mass. It was obtained from the
  StatLib archive (http://lib.stat.cmu.edu/datasets/boston), and has been used
  extensively throughout the literature to benchmark algorithms. However, these
  comparisons were primarily done outside of Delve and are thus somewhat
  suspect. The dataset is small in size with only 506 cases. The data was
  originally published by Harrison, D. and Rubinfeld, D.L. `Hedonic prices and
  the demand for clean air', J. Environ. Economics & Management, vol.5, 81-102,
  1978. """
  return {
    "data": Matrix(path=data.path, names_row=0, ignore=1, target="MEDV")
  }
  