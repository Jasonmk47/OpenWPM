import sklearn.datasets
import numpy
import scipy
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier


def main():
	dataset = sklearn.datasets.load_files('/home/jason/Desktop/NYT/analysis/sources', encoding="utf-8", decode_error='ignore')

	count_vect = CountVectorizer()
	training_counts = count_vect.fit_transform(dataset.data)
	training_counts.shape

	tf_transformer = TfidfTransformer(use_idf=True).fit(training_counts)
	training_tf = tf_transformer.transform(training_counts)
	training_tf.shape

	support_vector_machine = svm.SVC(kernel='linear')
	support_vector_machine.fit(training_tf, dataset.target)

	naive_bayes = MultinomialNB().fit(training_tf, dataset.target)

	linear_svm = Pipeline([('vect', count_vect),('tfidf',tf_transformer),('clf',SGDClassifier(loss='hinge',alpha=1e-3,n_iter=5,random_state=42)),])
	linear_svm.fit(dataset.data, dataset.target)

	test_dataset = sklearn.datasets.load_files('/home/jason/Desktop/NYT/analysis/test_articles', encoding="utf-8", decode_error='ignore')
	new_counts = count_vect.transform(test_dataset.data)
	new_tfidf = tf_transformer.transform(new_counts)


	svm_prediction = support_vector_machine.predict(new_tfidf)
	nb_prediction = naive_bayes.predict(new_tfidf)
	#lsvm_prediction = linear_svm.predict(new_tfidf)

	print "actual"
	print test_dataset.target

	print "svm prediction: "
	print svm_prediction


	mapping = dict(zip(count_vect.get_feature_names(), tf_transformer.idf_))

	print "coefficients"
	print support_vector_machine.coef_

	print " training set"
	print training_tf



	print "nb prediction: "
	print nb_prediction
	#print "Linear svm prediction: "
	#print lsvm_prediction


if __name__ == '__main__':
	main()