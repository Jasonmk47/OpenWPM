import sklearn.datasets
import numpy
import scipy
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_curve, auc


def main():
	dataset = sklearn.datasets.load_files('/home/jason/Desktop/NYT/analysis/sources', encoding="utf-8", decode_error='ignore')

	count_vect = CountVectorizer()
	training_counts = count_vect.fit_transform(dataset.data)
	training_counts.shape

	tf_transformer = TfidfTransformer(use_idf=True).fit(training_counts)
	training_tf = tf_transformer.transform(training_counts)
	training_tf.shape

	support_vector_machine = svm.SVC(kernel='linear', probability=True)

	support_vector_machine.fit(training_tf, dataset.target)

	test_dataset = sklearn.datasets.load_files('/home/jason/Desktop/NYT/analysis/test_articles', encoding="utf-8", decode_error='ignore')
	new_counts = count_vect.transform(test_dataset.data)
	new_tfidf = tf_transformer.transform(new_counts)

	svm_prediction = support_vector_machine.predict(new_tfidf)
	svm_proba_prediction = support_vector_machine.predict_proba(new_tfidf)


	score = support_vector_machine.decision_function(new_tfidf)
	fpr = dict()
	tpr = dict()
	roc_auc = dict()

	print "score: "
	print score



	print "actual"
	print test_dataset.target

	print "svm prediction: "
	print svm_prediction


	print "svm probabilities"
	for point in svm_proba_prediction:
		print "%.8f" % point[0]
		print "%.8f" % point[1]



if __name__ == '__main__':
	main()