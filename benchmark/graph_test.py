from statistics import mean

import matplotlib.pyplot as plt
import numpy as np
from json import load
from os import listdir

import test


def plot_map(source_dir, files_name):
    plt.clf()
    y_cord = []
    for file in files_name:
        with open(source_dir + '/' + file) as json_file:
            if file == 'TF_IDF.json':
                data = load(json_file)
                relevant_array = data['averagePrec']
                y_cord.append(mean(relevant_array))
            if file == 'BM25F.json':
                data = load(json_file)
                relevant_array = data['averagePrec']
                y_cord.append(mean(relevant_array))


    x_cord = [1, 2]

    # plotting a bar chart
    plt.bar(
        x_cord,
        y_cord,
        tick_label=['BM25F','TF_IDF'],
        width=0.8,
        color=['tab:orange', 'tab:blue'])

    # naming the x-axis
    plt.xlabel('Scoring Algorithms')
    # naming the y-axis
    plt.ylabel('Average Precision')
    # plot title
    plt.title('Mean Average Precision')

    plt.savefig('plot-data/MAP.png')


def plot_ap_srl(source_dir, files_name):
    plt.clf()

    for file in files_name:
        y_cord = []
        with open(source_dir + '/' + file) as json_file:
            data = load(json_file)

        relevant_array = data['averagePrec']

        i = 0
        while i < 10:
            y_cord.append(relevant_array[i])
            i += 1


        x_cord = [x * 0.1 for x in range(0, 10)]
        plt.plot(x_cord, y_cord, label=file[:-5])

    # naming the x axis
    plt.xlabel('Recall Levels')
    # naming the y axis
    plt.ylabel('Average Precision')
    # giving a title to my graph

    map =  round(mean(relevant_array), 2)


    #plt.title(f'* Mean Average Precision {map} *\n Average Precision with Standard Recall Levels')
    plt.title('Average Precision with Standard Recall Levels')

    # show a legend on the plot
    plt.legend()
    plt.ylim(ymin=0)

    plt.savefig('plot-data/AP-SRL.png')




if __name__ == '__main__':
    source_dir = 'json-data-test'
    files_name = listdir(source_dir)

    plot_ap_srl(source_dir, files_name)
    plot_map(source_dir,files_name)

