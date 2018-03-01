'''
Script to help visualize the results of the trained model

Author : Anirudh Vemula
Date : 10th November 2016
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
import pickle
import seaborn as sns
from numpy import linalg as LA


def plot_trajectories(true_trajs, pred_trajs, obs_length, name):
    '''
    Function that plots the true trajectories and the
    trajectories predicted by the model alongside
    params:
    true_trajs : numpy matrix with points of the true trajectories
    pred_trajs : numpy matrix with points of the predicted trajectories
    Both parameters are of shape traj_length x maxNumPeds x 3
    obs_length : Length of observed trajectory
    name: Name of the plot
    '''
    traj_length, maxNumPeds, _ = true_trajs.shape

    # Initialize figure
    # fig = plt.figure()
    # ax1 = fig.add_subplot(2, 1, 1)
    # ax2 = fig.add_subplot(2, 1, 2)

    # f, (ax1, ax2) = plt.subplots(2, 1, sharey=True, sharex=True)
    fig1 = plt.figure()
    # fig2 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    # ax2 = fig2.add_subplot(1, 1, 1)

    # Load the background
    im = plt.imread('plot/background.png')
    width = im.shape[0]
    height = im.shape[1]

    limits_x = []
    limits_y = []

    ped_x  = []
    ped_y = []

    traj_data = {}
    pred_data = {}
    obs_data = {}
    pred_data = []
    pred_cov_data = []
    obs_data = []
    obs_samples_lem=0
    # For each frame/each point in all trajectories
    for j in range(maxNumPeds):

        # For each pedestrian
        for i in range(traj_length):
            # pred_pos = pred_[i, :]
            true_pos = true_trajs[i, :]

            ped=true_pos[j][0]
            ped = pred_trajs[i][j][0]
            if true_pos[j][0] == 0:
                # Not a ped
                continue
            #elif pred_trajs[0][i][j][0] == 0:
            elif pred_trajs[i][j][0] == 0:
                # Not a ped
                continue
            else:
                # if is out of the map
                #if true_pos[j, 1] > 1 or true_pos[j, 1] < -1:
                #    continue
                #elif true_pos[j, 2] > 1 or true_pos[j, 2] < -1:
                #    continue

                if (j not in traj_data) and i < obs_length:
                    traj_data[j] = []
                fran=False
                if True:
                    traj_data[j].append(list(true_pos[j, 1:3]))
                    if fran:
                        for index, sample in enumerate(pred_trajs):
                            if i >= obs_length:
                                pred_data[j].append(list(sample[i][j,1:3]))
                            else:
                                obs_data[j].append(list(sample[i][j, 1:3]))
                    else:
                        if true_pos[j, 0]==1:
                            if i >= obs_length:
                                pred_data.append(list(pred_trajs[i][j][1:3]))
                                pred_cov_data.append(list(pred_trajs[i][j][3:6]))
                            else:
                                obs_data.append(list(pred_trajs[i][j][1:3]))
                        # traj_data[j][1].append(pred_pos[j, 1:3])
    true_x=np.zeros(traj_length)
    true_y=np.zeros(traj_length)
    pred_x=np.zeros(traj_length-obs_length)
    pred_y=np.zeros(traj_length-obs_length)
    obs_x=np.zeros(obs_length)
    obs_y=np.zeros(obs_length)
    for j in range(1,len(traj_data)):
        if j in traj_data:
            for i in range(len(traj_data[j])):
                true_x[i] = (1. + traj_data[j][i][0]) * width / 2.
                true_y[i] = (1. + traj_data[j][i][1]) * height / 2.
                if i>= obs_length:
                    pred_x[i-8] = (1. + pred_data[i-8][0]) * width / 2.
                    pred_y[i-8] = (1. + pred_data[i-8][1]) * height / 2.
                if i < obs_length:
                    obs_x[i] = (1. + obs_data[i][0]) * width / 2.
                    obs_y[i] = (1. + obs_data[i][1]) * height / 2.

                label1 = 'Pedestrian observed states'
                label2 = 'Pedestrian no-observed states'

                limits_x=pred_x
                limits_y=pred_y
                obs_samples_lem = len(limits_x)
                label1 = 'Robot observed states'
                label2 = 'Robot predicted states'
                label3 = 'Robot real states'
                label4 = 'Other Pedestrians'
                # Ploting predicted trajectories for time t till t+12
                x=len(pred_x)
            if pred_x[0] >0:
                ax1.plot(obs_x[obs_x !=0], obs_y[obs_y !=0], color='g',linestyle='solid', marker='o', label=label1)
                #Predicted trajectories
                ax1.plot(pred_x[pred_x !=0], pred_y[pred_y !=0], color='b', linestyle='solid', marker='o', label=label2)
                ax1.plot(true_x[true_x !=0], true_y[true_y !=0], color='b', linestyle='solid', marker='_', label=label3)
                sns.kdeplot(pred_x[pred_x !=0], pred_y[pred_y !=0], shade=True, ax=ax1, shade_lowest=False, cmap="Blues")
                #sns.kdeplot(limits_x[obs_samples_lem:len(limits_x)], limits_y[obs_samples_lem:len(limits_x)],
                #            shade=True, ax=ax1, shade_lowest=False)
            else:
                # Ploting real/observed trajectory from t till t+8
                ax1.plot(true_x[true_x !=0], true_y[true_y !=0], color='r',linestyle='solid', marker='o', label=label4)
            # ax2.plot(true_x[0:min(obs_length, len(true_x))], true_y[0:min(obs_length,len(true_y))], color=c, linestyle='solid', marker='o', label=label1)
        ax1.imshow(im)
        leg1 = ax1.legend(loc='lower right', shadow=True)
        ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
        true_x = np.zeros(traj_length)
        true_y = np.zeros(traj_length)
        pred_x = np.zeros(traj_length - obs_length)
        pred_y = np.zeros(traj_length - obs_length)
        obs_x = np.zeros(obs_length)
        obs_y = np.zeros(obs_length)
    plt.show()
    #plt.close()


def main():
    '''
    Main function
    '''
    f = open('save/012345/social_results.pkl', 'rb')
    results = pickle.load(f)
    fran=False

    for i in range(len(results)):

        name = 'sequence' + str(i)
        if fran:
            plot_trajectories(results[i][0][0], results[i][1:-1], results[i][0][1], name)
        else:                    #header         #first sampled traj     #number obbservations
            plot_trajectories(results[i][0][0], results[i][3], results[i][0][1], name)



if __name__ == '__main__':
    main()
