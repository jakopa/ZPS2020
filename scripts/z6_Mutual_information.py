from sklearn import datasets, metrics, feature_selection
from functools import partial
import time
import pickle

def read_data(input_dir):
    # wczytujemy dane treningowe:
    train_data_infile = open(input_dir + '/train_data.pkl', 'rb')  # czytanie z pliku
    data_train_all_dict = pickle.load(train_data_infile)

    x_train = data_train_all_dict["data"]
    y_train = data_train_all_dict["classes"]

    # wczytujemy dane testowe:
    test_data_infile = open(input_dir + '/test_data.pkl', 'rb')  # czytanie z pliku
    data_test_all_dict = pickle.load(test_data_infile)

    x_test = data_test_all_dict["data"]

    y_test = data_test_all_dict["classes"]

    # i nazwy klas
    cl_names_infile = open(input_dir + '/class_names.pkl', 'rb')
    classes_names = pickle.load(cl_names_infile)

    print("Data loaded from " + input_dir)

    return x_train, y_train, x_test, y_test, classes_names


def save_data(x_train, y_train, x_test, y_test, classes_names, output_dir):
    # zapisujemy dane treningowe
    x_train_all_dict = {'data': x_train,
                        'classes': y_train}

    train_data_outfile = open(output_dir + '/train_data.pkl', 'wb')
    pickle.dump(x_train_all_dict, train_data_outfile)

    # zapisujemy dane testowe
    x_test_all_dict = {'data': x_test,
                       'classes': y_test}

    test_data_outfile = open(output_dir + '/test_data.pkl', 'wb')
    pickle.dump(x_test_all_dict, test_data_outfile)

    # zapisujemy nazwy klas
    cl_names_outfile = open(output_dir + '/class_names.pkl', 'wb')
    pickle.dump(classes_names, cl_names_outfile)

    print("Pickles saved in ", output_dir)


input_dir = input("Adres pliku:")

x_train,y_train, x_test,y_test,classes_names = read_data(input_dir)

print("Twoje dane mają rozmiar:",x_train.shape[1])

n_comp = input('Nowy wymiar:')

fs = feature_selection.SelectKBest(score_func=partial(feature_selection.mutual_info_classif, n_neighbors=3), k=int(n_comp))
start_time = time.time()
x_train_reduced = fs.fit_transform(x_train,y_train)
print("  took %s seconds " % round((time.time() - start_time),5))
x_test_reduced = fs.transform(x_test)

print('Gdzie chcesz zapisać wynik?')
output_dir = input('Adres do zapisu:')
save_data(x_train_reduced, y_train, x_test_reduced, y_test, classes_names, output_dir)

fs_object_file = open(output_dir+"/fs_IM_object.pkl", "wb")
pickle.dump(fs,fs_object_file)
