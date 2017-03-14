#Thompson Model

#importing the dataset
dataset<-read.csv('/Users/DK/Documents/Machine_Learning/Python-and-R/Machine_Learning_Projects/Reinforcement Learning/Thompson Model/Ads_CTR_Optimisation.csv')

#implementing Thompson Model
N<-10000
d<-10
total_reward<-0
selected_ads<-integer(0)
num_of_rewards_1<-integer(d)
num_of_rewards_0<-integer(d)

for (n in 1:N){
  max_random<-0
  ad<-0
  for (i in 1:d){
    random_beta<-rbeta(n=1,num_of_rewards_1[i]+1,num_of_rewards_0[i]+1)
    if(random_beta>max_random){
      max_random<-random_beta
      ad<-i
    }
  }
  selected_ads<-append(selected_ads,ad)
  reward<-dataset[n,ad]
  if(reward==1){
    num_of_rewards_1[ad]<-num_of_rewards_1[ad]+ 1
  }
  else{
    num_of_rewards_0[ad]=num_of_rewards_0[ad]+1
  }
  total_reward<-total_reward+reward
}

#visualisation
hist(selected_ads,
     col='blue',
     main='Histogram of Selected Ads',
     xlab='Ads',
     ylab='Number of times each ad was selected')
