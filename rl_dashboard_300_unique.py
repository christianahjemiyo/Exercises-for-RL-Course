import streamlit as st
import random
from collections import Counter

st.set_page_config(page_title="RL Course Practice Dashboard", layout="wide")

QUESTIONS = [
  {
    "question": "A card-game agent updates only after the final outcome of each hand is known. Which algorithm family best matches this setup?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "SARSA",
      "DQN"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo waits for the episode to finish before updating.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which algorithm is most natural when you can observe the full return from a short episodic task like Blackjack?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Q-learning",
      "DDPG"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo uses complete returns and fits short episodic tasks well.",
    "category": "Monte Carlo"
  },
  {
    "question": "An RL method estimates state values using the total sampled return G_t rather than bootstrapping from V(s'). Which method is this?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "TD(λ)",
      "Actor-Critic"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo uses full sampled returns instead of bootstrap targets.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which approach does not require an estimate of the next state's value during its basic update?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Q-learning",
      "DQN"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo updates from complete returns and does not bootstrap.",
    "category": "Monte Carlo"
  },
  {
    "question": "An environment has clear episode boundaries, and delayed updates are acceptable. Which family is a good first choice for learning from sampled experience?",
    "options": [
      "Monte Carlo",
      "TD(n)",
      "SARSA",
      "PPO"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo is appropriate when episodes end clearly and delayed learning is acceptable.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which method is generally higher variance because it relies on full sampled returns?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "A2C/A3C",
      "TD3"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo tends to have higher variance than TD methods.",
    "category": "Monte Carlo"
  },
  {
    "question": "If lambda moves all the way toward 1 in the TD(λ) intuition, which style of target does learning become closer to?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Q-learning",
      "DDPG"
    ],
    "answer": "Monte Carlo",
    "explanation": "As lambda approaches 1, TD(λ) behaves more like Monte Carlo.",
    "category": "Monte Carlo"
  },
  {
    "question": "A student says, 'I want learning targets that use every remaining reward until termination.' Which method are they describing?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "TRPO",
      "DDPG"
    ],
    "answer": "Monte Carlo",
    "explanation": "That description matches Monte Carlo returns.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which algorithm family is easiest to explain as 'learn from complete episodes, then average what happened'?",
    "options": [
      "Monte Carlo",
      "TD(λ)",
      "SARSA",
      "SAC"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo learns from completed episodes.",
    "category": "Monte Carlo"
  },
  {
    "question": "For an episodic board game simulation, which method avoids bootstrap bias by using the realized return?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Q-learning",
      "Actor-Critic"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo uses the realized return rather than a bootstrap estimate.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which learning method becomes awkward when there is no natural end to an interaction and episodes may be extremely long?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "PPO",
      "DDPG"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo depends on episode completion, so continuing tasks are awkward.",
    "category": "Monte Carlo"
  },
  {
    "question": "You need a baseline algorithm for an assignment where the professor emphasizes 'full return after termination.' What is the most likely answer?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Q-learning",
      "DQN"
    ],
    "answer": "Monte Carlo",
    "explanation": "That wording points directly to Monte Carlo.",
    "category": "Monte Carlo"
  },
  {
    "question": "In a maze task, the agent stores the entire episode and updates only after reaching the goal or failing. Which method is it closest to?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "SARSA",
      "TD3"
    ],
    "answer": "Monte Carlo",
    "explanation": "Updating only after the episode ends is Monte Carlo style.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which family uses sample returns without bootstrapping and therefore often learns more slowly online?",
    "options": [
      "Monte Carlo",
      "TD(n)",
      "Q-learning",
      "A2C/A3C"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo uses sample returns without bootstrap targets.",
    "category": "Monte Carlo"
  },
  {
    "question": "A professor asks which method can be understood before Bellman bootstrapping is introduced. Which option best fits?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Q-learning",
      "SAC"
    ],
    "answer": "Monte Carlo",
    "explanation": "Monte Carlo is often taught before TD because it does not rely on bootstrapping.",
    "category": "Monte Carlo"
  },
  {
    "question": "If your estimate target is G_t = R_{t+1} + Î³R_{t+2} + ... until terminal time, which family are you using?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "PPO",
      "DDPG"
    ],
    "answer": "Monte Carlo",
    "explanation": "That is the Monte Carlo return.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which method is often paired with importance sampling for off-policy episodic evaluation in introductory RL?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Q-learning",
      "TD3"
    ],
    "answer": "Monte Carlo",
    "explanation": "Off-policy Monte Carlo commonly uses importance sampling.",
    "category": "Monte Carlo"
  },
  {
    "question": "An agent learns from ten finished episodes of a racing game by averaging observed returns from visited states. Which approach is this?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "REINFORCE",
      "DQN"
    ],
    "answer": "Monte Carlo",
    "explanation": "Averaging observed returns from finished episodes is Monte Carlo.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which option best matches the phrase 'no bootstrap, just sample the return'?",
    "options": [
      "Monte Carlo",
      "TD(0)",
      "Actor-Critic",
      "SAC"
    ],
    "answer": "Monte Carlo",
    "explanation": "That is the defining intuition of Monte Carlo.",
    "category": "Monte Carlo"
  },
  {
    "question": "Which method updates a state estimate immediately using r + Î³V(s') as the target?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "REINFORCE",
      "PPO"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) uses a one-step bootstrap target.",
    "category": "TD Learning"
  },
  {
    "question": "An agent learns online after every transition and uses the next state's estimated value. Which algorithm is this most directly?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "DDPG",
      "SAC"
    ],
    "answer": "TD(0)",
    "explanation": "That is the defining pattern of TD(0).",
    "category": "TD Learning"
  },
  {
    "question": "Which algorithm sits at the simplest end of the temporal-difference family?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "DQN",
      "TRPO"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) is the canonical one-step TD method.",
    "category": "TD Learning"
  },
  {
    "question": "A value update is based on one observed reward plus one bootstrap term. Which method does that describe?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "Q-learning",
      "TD3"
    ],
    "answer": "TD(0)",
    "explanation": "One reward plus one bootstrap term is TD(0).",
    "category": "TD Learning"
  },
  {
    "question": "Which method is appropriate when you cannot wait until the episode ends and want step-by-step value learning?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "REINFORCE",
      "DDPG"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) learns during the episode.",
    "category": "TD Learning"
  },
  {
    "question": "If the target is R_{t+1} + Î³V(S_{t+1}), which algorithm is being used?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "TD(λ)",
      "PPO"
    ],
    "answer": "TD(0)",
    "explanation": "That is the TD(0) target.",
    "category": "TD Learning"
  },
  {
    "question": "Which method is lower variance than Monte Carlo because it bootstraps from current estimates?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "SAC",
      "DDPG"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) reduces variance via bootstrapping.",
    "category": "TD Learning"
  },
  {
    "question": "A robot navigation problem runs for long stretches, so learning must occur after each move. Which basic algorithm family fits best?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "TRPO",
      "DQN"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) is a natural basic online method.",
    "category": "TD Learning"
  },
  {
    "question": "Which algorithm family is commonly introduced as 'bootstrapping from the very next state only'?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "TD3",
      "SAC"
    ],
    "answer": "TD(0)",
    "explanation": "That is TD(0).",
    "category": "TD Learning"
  },
  {
    "question": "If lambda = 0 in TD(λ), which method do you recover?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "Q-learning",
      "DDPG"
    ],
    "answer": "TD(0)",
    "explanation": "TD(λ) with lambda = 0 reduces to TD(0).",
    "category": "TD Learning"
  },
  {
    "question": "Which method often serves as the bridge between Monte Carlo intuition and more advanced control methods?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "PPO",
      "TD3"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) introduces bootstrapping and online learning.",
    "category": "TD Learning"
  },
  {
    "question": "Which option is best for continuing tasks where episodes may not terminate for a long time?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "REINFORCE",
      "TRPO"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) does not need the episode to finish before learning.",
    "category": "TD Learning"
  },
  {
    "question": "A professor writes Î´_t = R_{t+1} + Î³V(S_{t+1}) âˆ’ V(S_t). Which algorithm is most directly associated with this error term?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "SAC",
      "DDPG"
    ],
    "answer": "TD(0)",
    "explanation": "That temporal-difference error is the classic TD(0) form.",
    "category": "TD Learning"
  },
  {
    "question": "Which method is usually more data-efficient online than Monte Carlo because it updates every step?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "DQN",
      "PPO"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) updates at each transition.",
    "category": "TD Learning"
  },
  {
    "question": "You want the simplest possible bootstrap learner for state values, not action values. Which option fits?",
    "options": [
      "TD(0)",
      "Q-learning",
      "SARSA",
      "DQN"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) is the simplest one-step value estimator.",
    "category": "TD Learning"
  },
  {
    "question": "An assignment asks for a prediction method rather than a control method, using one-step returns. Which answer is best?",
    "options": [
      "TD(0)",
      "Q-learning",
      "SARSA",
      "DDPG"
    ],
    "answer": "TD(0)",
    "explanation": "Prediction with one-step returns points to TD(0).",
    "category": "TD Learning"
  },
  {
    "question": "Which algorithm uses bootstrapping but not the max operator over actions?",
    "options": [
      "TD(0)",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) bootstraps state values without maximizing over actions.",
    "category": "TD Learning"
  },
  {
    "question": "A student describes an approach as 'faster feedback than Monte Carlo, but more biased because it trusts its current estimate.' Which algorithm fits?",
    "options": [
      "TD(0)",
      "Monte Carlo",
      "TRPO",
      "SAC"
    ],
    "answer": "TD(0)",
    "explanation": "That is the classic TD(0) tradeoff.",
    "category": "TD Learning"
  },
  {
    "question": "Which method best matches the phrase 'one-step lookahead value learning'?",
    "options": [
      "TD(0)",
      "TD(n)",
      "PPO",
      "Actor-Critic"
    ],
    "answer": "TD(0)",
    "explanation": "TD(0) uses a one-step lookahead target.",
    "category": "TD Learning"
  },
  {
    "question": "Which method uses n observed rewards before bootstrapping from a later value estimate?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Monte Carlo",
      "PPO"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) accumulates n rewards before bootstrapping.",
    "category": "TD Learning"
  },
  {
    "question": "A target of R_{t+1} + Î³R_{t+2} + ... + Î³^{n-1}R_{t+n} + Î³^nV(S_{t+n}) corresponds to which method?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Monte Carlo",
      "SAC"
    ],
    "answer": "TD(n)",
    "explanation": "That is the n-step TD target.",
    "category": "TD Learning"
  },
  {
    "question": "Which approach lies between TD(0) and Monte Carlo because it waits a few steps but not necessarily until the end?",
    "options": [
      "TD(n)",
      "TD(0)",
      "TRPO",
      "DDPG"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) interpolates between one-step TD and full-return Monte Carlo.",
    "category": "TD Learning"
  },
  {
    "question": "A student wants less bias than TD(0) but less variance than full Monte Carlo. Which method family should they consider first?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Monte Carlo",
      "DQN"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) offers a tradeoff between TD(0) and Monte Carlo.",
    "category": "TD Learning"
  },
  {
    "question": "Which method becomes TD(0) when n = 1?",
    "options": [
      "TD(n)",
      "Monte Carlo",
      "SAC",
      "TD3"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) with n=1 is TD(0).",
    "category": "TD Learning"
  },
  {
    "question": "Which method becomes closer to Monte Carlo as n approaches the remaining episode length?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Q-learning",
      "DDPG"
    ],
    "answer": "TD(n)",
    "explanation": "Large n-step targets resemble Monte Carlo returns.",
    "category": "TD Learning"
  },
  {
    "question": "An assignment asks for a prediction method that stores a short rollout before updating. Which option best fits?",
    "options": [
      "TD(n)",
      "Q-learning",
      "SARSA",
      "PPO"
    ],
    "answer": "TD(n)",
    "explanation": "Storing a short rollout before bootstrapping is TD(n).",
    "category": "TD Learning"
  },
  {
    "question": "Which method is useful when one-step feedback is too myopic but full-episode returns are unnecessarily delayed?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Monte Carlo",
      "TRPO"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) is designed for that middle ground.",
    "category": "TD Learning"
  },
  {
    "question": "A learning rule references an 'n-step return.' Which family is the obvious answer?",
    "options": [
      "TD(n)",
      "TD(0)",
      "DQN",
      "SAC"
    ],
    "answer": "TD(n)",
    "explanation": "That phrase directly identifies TD(n).",
    "category": "TD Learning"
  },
  {
    "question": "Which method can be viewed as a finite-horizon compromise between immediate bootstrapping and waiting until termination?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Monte Carlo",
      "DDPG"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) is exactly that compromise.",
    "category": "TD Learning"
  },
  {
    "question": "In practice, why might someone choose a small n greater than 1? To capture what kind of information?",
    "options": [
      "TD(n)",
      "TD(0)",
      "TRPO",
      "DQN"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) can capture slightly longer-term reward structure before bootstrapping.",
    "category": "TD Learning"
  },
  {
    "question": "Which method uses multi-step targets without averaging over all possible step lengths like TD(λ) does?",
    "options": [
      "TD(n)",
      "TD(λ)",
      "TD(0)",
      "PPO"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) chooses one specific step length.",
    "category": "TD Learning"
  },
  {
    "question": "If the professor asks for 'a specific multi-step TD target,' which answer is more precise than saying TD(λ)?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Monte Carlo",
      "Actor-Critic"
    ],
    "answer": "TD(n)",
    "explanation": "A fixed multi-step target is TD(n), not the lambda-weighted mixture.",
    "category": "TD Learning"
  },
  {
    "question": "A value function learner takes three rewards, then bootstraps from the fourth state's value. Which method is that conceptually?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Monte Carlo",
      "DQN"
    ],
    "answer": "TD(n)",
    "explanation": "That is a 3-step TD target, i.e., TD(n).",
    "category": "TD Learning"
  },
  {
    "question": "Which method is most naturally described as using a rollout window of fixed length n?",
    "options": [
      "TD(n)",
      "TD(0)",
      "Q-learning",
      "TD3"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) uses a fixed rollout length before bootstrapping.",
    "category": "TD Learning"
  },
  {
    "question": "Compared with TD(0), which method may propagate reward information faster across several earlier states in one update?",
    "options": [
      "TD(n)",
      "TD(0)",
      "REINFORCE",
      "DDPG"
    ],
    "answer": "TD(n)",
    "explanation": "Multi-step TD can move reward information back more quickly.",
    "category": "TD Learning"
  },
  {
    "question": "A tutorial explains that you can choose n=4, n=5, or n=10 depending on the problem. Which family is being discussed?",
    "options": [
      "TD(n)",
      "TD(0)",
      "PPO",
      "SAC"
    ],
    "answer": "TD(n)",
    "explanation": "That tuning language refers to TD(n).",
    "category": "TD Learning"
  },
  {
    "question": "Which method is better matched to the phrase 'fixed-horizon bootstrapping'?",
    "options": [
      "TD(n)",
      "Monte Carlo",
      "TRPO",
      "TD3"
    ],
    "answer": "TD(n)",
    "explanation": "TD(n) bootstraps after a fixed number of steps.",
    "category": "TD Learning"
  },
  {
    "question": "Which algorithm combines many n-step returns using a decay parameter lambda?",
    "options": [
      "TD(λ)",
      "TD(n)",
      "TD(0)",
      "Monte Carlo"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) blends n-step returns with lambda-weighting.",
    "category": "TD Learning"
  },
  {
    "question": "Which method is most closely tied to eligibility traces?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "Q-learning",
      "PPO"
    ],
    "answer": "TD(λ)",
    "explanation": "Eligibility traces are a hallmark of TD(λ).",
    "category": "TD Learning"
  },
  {
    "question": "A student wants one framework that smoothly bridges TD(0) and Monte Carlo. Which method is it?",
    "options": [
      "TD(λ)",
      "TD(n)",
      "DQN",
      "SAC"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) interpolates between TD(0) and Monte Carlo.",
    "category": "TD Learning"
  },
  {
    "question": "When lambda = 0, which blended method collapses to one-step TD behavior?",
    "options": [
      "TD(λ)",
      "Monte Carlo",
      "DDPG",
      "TRPO"
    ],
    "answer": "TD(λ)",
    "explanation": "That statement defines TD(λ).",
    "category": "TD Learning"
  },
  {
    "question": "When lambda is close to 1, which method behaves more like learning from long returns?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "Q-learning",
      "DQN"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) approaches Monte Carlo-like targets as lambda increases.",
    "category": "TD Learning"
  },
  {
    "question": "Which method is appropriate when you want a weighted mixture of short- and long-horizon credit assignment?",
    "options": [
      "TD(λ)",
      "TD(n)",
      "TD(0)",
      "SAC"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) mixes different backup lengths.",
    "category": "TD Learning"
  },
  {
    "question": "A professor says, 'Donâ€™t pick a single n; average over many n-step targets.' Which method does that describe?",
    "options": [
      "TD(λ)",
      "TD(n)",
      "Monte Carlo",
      "DDPG"
    ],
    "answer": "TD(λ)",
    "explanation": "That is exactly the TD(λ) idea.",
    "category": "TD Learning"
  },
  {
    "question": "Which algorithm is often implemented with backward-view traces that decay over time?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "PPO",
      "TD3"
    ],
    "answer": "TD(λ)",
    "explanation": "Backward-view eligibility traces are standard for TD(λ).",
    "category": "TD Learning"
  },
  {
    "question": "If recent states should receive more credit than distant ones through a decaying memory, which method fits best?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "Q-learning",
      "REINFORCE"
    ],
    "answer": "TD(λ)",
    "explanation": "Eligibility traces in TD(λ) create decaying credit assignment.",
    "category": "TD Learning"
  },
  {
    "question": "Which method is conceptually harder than TD(0) because it brings in traces and lambda-weighting?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "Monte Carlo",
      "DQN"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) adds the lambda trace mechanism.",
    "category": "TD Learning"
  },
  {
    "question": "An assignment asks for the algorithm family that unifies one-step and multi-step temporal-difference learning. Which answer is right?",
    "options": [
      "TD(λ)",
      "TD(n)",
      "TD(0)",
      "Actor-Critic"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) is the unifying lambda-weighted family.",
    "category": "TD Learning"
  },
  {
    "question": "Which algorithm is best identified by the phrase 'forward view vs backward view equivalence'?",
    "options": [
      "TD(λ)",
      "Monte Carlo",
      "SAC",
      "DDPG"
    ],
    "answer": "TD(λ)",
    "explanation": "That phrase is classic TD(λ) material.",
    "category": "TD Learning"
  },
  {
    "question": "Which method can speed reward propagation without committing to a single fixed rollout length n?",
    "options": [
      "TD(λ)",
      "TD(n)",
      "Q-learning",
      "PPO"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) averages over many rollout lengths.",
    "category": "TD Learning"
  },
  {
    "question": "A learner keeps a temporary memory for recently visited states and updates them proportionally when new errors arrive. Which method is this?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "DQN",
      "TD3"
    ],
    "answer": "TD(λ)",
    "explanation": "That describes eligibility traces in TD(λ).",
    "category": "TD Learning"
  },
  {
    "question": "Which family is the natural answer when someone asks about lambda controlling the span of credit assignment?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "Monte Carlo",
      "DDPG"
    ],
    "answer": "TD(λ)",
    "explanation": "lambda is the key parameter in TD(λ).",
    "category": "TD Learning"
  },
  {
    "question": "A student says 'I want a continuum from bootstrapping immediately to waiting almost until the end.' Which method are they describing?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "SAC",
      "TRPO"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) provides that continuum.",
    "category": "TD Learning"
  },
  {
    "question": "Which method is associated with replacing traces or accumulating traces in some implementations?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "Q-learning",
      "PPO"
    ],
    "answer": "TD(λ)",
    "explanation": "Those are implementation details of TD(λ)-style methods.",
    "category": "TD Learning"
  },
  {
    "question": "If the professor asks which method uses eligibility traces for temporal credit assignment, what should you answer?",
    "options": [
      "TD(λ)",
      "TD(n)",
      "DQN",
      "DDPG"
    ],
    "answer": "TD(λ)",
    "explanation": "The standard answer is TD(λ).",
    "category": "TD Learning"
  },
  {
    "question": "Which approach gives you lambda as a hyperparameter to tune the influence of longer returns?",
    "options": [
      "TD(λ)",
      "TD(0)",
      "Actor-Critic",
      "SAC"
    ],
    "answer": "TD(λ)",
    "explanation": "TD(λ) tunes that influence through lambda.",
    "category": "TD Learning"
  },
  {
    "question": "Which control algorithm updates Q using the action actually taken in the next state?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "PPO"
    ],
    "answer": "SARSA",
    "explanation": "SARSA uses the next action actually selected by the behavior policy.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is on-policy because it learns about the same policy it uses to act?",
    "options": [
      "SARSA",
      "Q-learning",
      "TD3",
      "SAC"
    ],
    "answer": "SARSA",
    "explanation": "SARSA is the classic on-policy TD control method.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "The update uses Q(S', A') instead of max_a Q(S', a). Which algorithm is this?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "DDPG"
    ],
    "answer": "SARSA",
    "explanation": "That is the defining SARSA update.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "In a risky cliff-walking problem, which algorithm often learns a safer policy under Îµ-greedy exploration because it accounts for exploratory actions?",
    "options": [
      "SARSA",
      "Q-learning",
      "TRPO",
      "SAC"
    ],
    "answer": "SARSA",
    "explanation": "SARSA learns values consistent with the exploratory policy, often making it safer.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which acronym stands for State-Action-Reward-State-Action?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "PPO"
    ],
    "answer": "SARSA",
    "explanation": "SARSA is named for the sequence in its update.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A learner wants the update target to depend on what the agent will actually do next, not the greedy best action. Which algorithm fits?",
    "options": [
      "SARSA",
      "Q-learning",
      "TD(0)",
      "Actor-Critic"
    ],
    "answer": "SARSA",
    "explanation": "That is SARSAâ€™s on-policy logic.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is a good teaching example for 'on-policy TD control'?",
    "options": [
      "SARSA",
      "Q-learning",
      "DDPG",
      "TD3"
    ],
    "answer": "SARSA",
    "explanation": "SARSA is the standard on-policy TD control example.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "If exploration noise should affect the learned action values directly, which algorithm is more appropriate: SARSA or Q-learning?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "PPO"
    ],
    "answer": "SARSA",
    "explanation": "SARSA includes exploratory action choices in its target.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method is commonly contrasted with Q-learning to explain on-policy versus off-policy learning?",
    "options": [
      "SARSA",
      "TD(0)",
      "DQN",
      "SAC"
    ],
    "answer": "SARSA",
    "explanation": "SARSA is the classic on-policy contrast to Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A professor asks for the algorithm that updates from the quintuple (S, A, R, S', A'). Which answer should you give?",
    "options": [
      "SARSA",
      "Q-learning",
      "DDPG",
      "TRPO"
    ],
    "answer": "SARSA",
    "explanation": "That notation directly names SARSA.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "In environments where unsafe exploratory actions matter, which algorithm may behave more conservatively during learning?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "SARSA",
    "explanation": "SARSA often learns safer values because it evaluates the exploratory policy.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which control algorithm would you pick if the policy being evaluated must be the current Îµ-greedy behavior policy?",
    "options": [
      "SARSA",
      "Q-learning",
      "DDPG",
      "SAC"
    ],
    "answer": "SARSA",
    "explanation": "That is precisely SARSA.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A student says, 'My target should be reward plus discounted value of the next action I really picked.' Which algorithm is that?",
    "options": [
      "SARSA",
      "Q-learning",
      "TD(0)",
      "PPO"
    ],
    "answer": "SARSA",
    "explanation": "That is the SARSA target.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method is better described as learning action values for the current behavior policy rather than directly for the optimal greedy policy?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "SARSA",
    "explanation": "SARSA learns about the current behavior policy.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm would likely be emphasized in class right after TD prediction when introducing control without max backup?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "SAC"
    ],
    "answer": "SARSA",
    "explanation": "SARSA extends TD ideas to on-policy control.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is often written as Q(s,a) â† Q(s,a) + Î±[r + Î³Q(s',a') âˆ’ Q(s,a)]?",
    "options": [
      "SARSA",
      "Q-learning",
      "DDPG",
      "PPO"
    ],
    "answer": "SARSA",
    "explanation": "That update equation is SARSA.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "For a tabular maze task with discrete actions, which method best matches 'on-policy action-value learning'?",
    "options": [
      "SARSA",
      "Q-learning",
      "TD(0)",
      "Actor-Critic"
    ],
    "answer": "SARSA",
    "explanation": "SARSA is the tabular on-policy action-value learner.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "If an exam question asks which algorithm incorporates the consequences of future exploration into its estimates, the safest answer is what?",
    "options": [
      "SARSA",
      "Q-learning",
      "DQN",
      "TRPO"
    ],
    "answer": "SARSA",
    "explanation": "SARSA accounts for future exploratory actions because it is on-policy.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is especially useful pedagogically for understanding why learned behavior can differ from an optimal greedy target?",
    "options": [
      "SARSA",
      "Q-learning",
      "SAC",
      "DDPG"
    ],
    "answer": "SARSA",
    "explanation": "SARSA highlights how learning follows the behavior policy.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm extends SARSA with eligibility traces?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "DQN"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) adds traces to on-policy TD control.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "If you want on-policy control plus faster multi-step credit assignment through traces, which method fits best?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "PPO"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) combines SARSA with eligibility traces.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method keeps the on-policy nature of SARSA while introducing a lambda parameter?",
    "options": [
      "SARSA(λ)",
      "Q-learning",
      "TD(0)",
      "SAC"
    ],
    "answer": "SARSA(λ)",
    "explanation": "That is SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A control algorithm uses the next action actually taken and also maintains eligibility traces. Which one is it?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "TD3"
    ],
    "answer": "SARSA(λ)",
    "explanation": "That describes SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is the natural answer to 'TD(λ) for action values under an on-policy control setup'?",
    "options": [
      "SARSA(λ)",
      "Q-learning",
      "DQN",
      "DDPG"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) is the on-policy control analogue.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A student wants recent state-action pairs to receive decaying credit after each TD error while remaining on-policy. Which algorithm should they choose?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "TRPO"
    ],
    "answer": "SARSA(λ)",
    "explanation": "Eligibility traces plus on-policy control means SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method would you mention if asked for a more advanced version of SARSA that can propagate rewards backward more quickly?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "DQN",
      "TD3"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) propagates reward information faster via traces.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which control algorithm can be viewed as blending multi-step on-policy returns for Q-values?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "DQN"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) blends multi-step on-policy information.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method retains the safer on-policy character of SARSA while improving temporal credit assignment?",
    "options": [
      "SARSA(λ)",
      "Q-learning",
      "SAC",
      "DDPG"
    ],
    "answer": "SARSA(λ)",
    "explanation": "That is SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "On an exam, which answer best fits: 'state-action traces plus on-policy control'?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "Actor-Critic"
    ],
    "answer": "SARSA(λ)",
    "explanation": "That phrase points to SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm can reduce the delay in propagating reward information compared with plain SARSA?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "PPO"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) uses traces to spread updates backward.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method is to SARSA what TD(λ) is to TD(0)?",
    "options": [
      "SARSA(λ)",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) is the lambda-trace extension of SARSA.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "If lambda=0 in SARSA(λ), what algorithm does the method reduce toward conceptually?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "DQN"
    ],
    "answer": "SARSA(λ)",
    "explanation": "This question is about the lambda-family around SARSA; lambda=0 recovers plain SARSA, so the family is SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is most appropriate when your professor says 'same as SARSA, but now add eligibility traces'?",
    "options": [
      "SARSA(λ)",
      "Q-learning",
      "DDPG",
      "SAC"
    ],
    "answer": "SARSA(λ)",
    "explanation": "That directly names SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A learner uses Q(S',A') as the target component and also updates a decaying trace for recent state-action pairs. Which algorithm is it?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "Q-learning",
      "DQN"
    ],
    "answer": "SARSA(λ)",
    "explanation": "That is the SARSA(λ) setup.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method would likely outperform plain SARSA in faster reward propagation while preserving on-policy learning assumptions?",
    "options": [
      "SARSA(λ)",
      "Q-learning",
      "PPO",
      "TD3"
    ],
    "answer": "SARSA(λ)",
    "explanation": "SARSA(λ) keeps on-policy learning but spreads credit faster.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which answer best matches 'eligibility traces for action-value control under the current behavior policy'?",
    "options": [
      "SARSA(λ)",
      "Q-learning",
      "DQN",
      "DDPG"
    ],
    "answer": "SARSA(λ)",
    "explanation": "That is SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "If a quiz asks for the lambda-based extension of an on-policy TD control algorithm, which choice should stand out?",
    "options": [
      "SARSA(λ)",
      "SARSA",
      "SAC",
      "TD3"
    ],
    "answer": "SARSA(λ)",
    "explanation": "The lambda-based extension of SARSA is SARSA(λ).",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which control algorithm uses the greedy target max_a Q(S', a) regardless of the action actually taken?",
    "options": [
      "Q-learning",
      "SARSA",
      "TD(0)",
      "PPO"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning is off-policy and uses the max backup.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is the textbook example of off-policy TD control?",
    "options": [
      "Q-learning",
      "SARSA",
      "DDPG",
      "SAC"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning is the classic off-policy TD control algorithm.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A learner wants to estimate the optimal action-value function directly while behaving Îµ-greedily. Which algorithm fits?",
    "options": [
      "Q-learning",
      "SARSA",
      "TD(0)",
      "Actor-Critic"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning learns toward the greedy optimal target.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method is often more aggressive than SARSA in cliff-walking because it assumes the best future action will be taken?",
    "options": [
      "Q-learning",
      "SARSA",
      "TD3",
      "TRPO"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning ignores exploratory actions in the target.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which update is correct for the algorithm? Q(s,a) â† Q(s,a) + Î±[r + Î³ max_a Q(s',a) âˆ’ Q(s,a)]",
    "options": [
      "Q-learning",
      "SARSA",
      "DQN",
      "PPO"
    ],
    "answer": "Q-learning",
    "explanation": "That is the standard Q-learning update.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is most appropriate when actions are discrete and you want a simple tabular route to an optimal policy?",
    "options": [
      "Q-learning",
      "DDPG",
      "SAC",
      "TRPO"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning is a standard choice for discrete tabular control.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method learns about a target policy different from the behavior policy?",
    "options": [
      "Q-learning",
      "SARSA",
      "Monte Carlo",
      "TD(0)"
    ],
    "answer": "Q-learning",
    "explanation": "That is the definition of off-policy learning, exemplified by Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "If exploratory moves should not directly define the learning target, which algorithm is usually preferred over SARSA?",
    "options": [
      "Q-learning",
      "SARSA",
      "Actor-Critic",
      "PPO"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning uses the greedy max target instead of the actual exploratory action.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is the conceptual parent of DQN?",
    "options": [
      "Q-learning",
      "SARSA",
      "TD(0)",
      "REINFORCE"
    ],
    "answer": "Q-learning",
    "explanation": "DQN is deep Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A professor asks for the algorithm that combines TD learning with greedy policy improvement through a max operator. Which answer is correct?",
    "options": [
      "Q-learning",
      "SARSA",
      "TRPO",
      "TD3"
    ],
    "answer": "Q-learning",
    "explanation": "That is Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method is best described as 'learn the value of the best action even while you explore using another policy'?",
    "options": [
      "Q-learning",
      "SARSA",
      "DQN",
      "SAC"
    ],
    "answer": "Q-learning",
    "explanation": "That is the off-policy idea behind Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "For a discrete-action maze, which algorithm is often the first serious control baseline students implement?",
    "options": [
      "Q-learning",
      "DDPG",
      "TRPO",
      "SAC"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning is the standard discrete-action control baseline.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is more likely than SARSA to hug the cliff in the classic cliff-walking example?",
    "options": [
      "Q-learning",
      "SARSA",
      "PPO",
      "Actor-Critic"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning learns the greedy optimal target and may take riskier paths.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method estimates action values for the optimal greedy policy, not necessarily for the policy currently generating data?",
    "options": [
      "Q-learning",
      "SARSA",
      "TD(0)",
      "Monte Carlo"
    ],
    "answer": "Q-learning",
    "explanation": "That is Q-learningâ€™s central property.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm would you pick for tabular control if your exam specifically mentions an off-policy max backup?",
    "options": [
      "Q-learning",
      "SARSA",
      "DDPG",
      "TD3"
    ],
    "answer": "Q-learning",
    "explanation": "Off-policy max backup clearly indicates Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "If the behavior policy is Îµ-greedy but the target policy is greedy, which algorithm most likely underlies the update?",
    "options": [
      "Q-learning",
      "SARSA",
      "DQN",
      "Actor-Critic"
    ],
    "answer": "Q-learning",
    "explanation": "That is the standard Q-learning setup.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which method commonly converges to optimal action values in tabular settings under appropriate conditions?",
    "options": [
      "Q-learning",
      "SARSA",
      "PPO",
      "DDPG"
    ],
    "answer": "Q-learning",
    "explanation": "Q-learning is the classic tabular optimal-control algorithm.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "A student says, 'I do not care about the next action actually sampled; I want the best one according to my table.' Which algorithm is this?",
    "options": [
      "Q-learning",
      "SARSA",
      "TD(0)",
      "SAC"
    ],
    "answer": "Q-learning",
    "explanation": "That statement describes Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is usually the right answer when the phrase 'Bellman optimality backup' appears in a tabular control question?",
    "options": [
      "Q-learning",
      "SARSA",
      "Actor-Critic",
      "TD3"
    ],
    "answer": "Q-learning",
    "explanation": "The Bellman optimality backup underlies Q-learning.",
    "category": "SARSA and Q-learning"
  },
  {
    "question": "Which algorithm is the classic Monte Carlo policy-gradient method?",
    "options": [
      "REINFORCE",
      "PPO",
      "Q-learning",
      "DQN"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE is the canonical Monte Carlo policy-gradient algorithm.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which method directly updates policy parameters using sampled returns and log-probability gradients?",
    "options": [
      "REINFORCE",
      "TD(0)",
      "Q-learning",
      "SAC"
    ],
    "answer": "REINFORCE",
    "explanation": "That is the REINFORCE update principle.",
    "category": "Policy Gradient"
  },
  {
    "question": "A learner does not want to estimate Q-values first and instead wants to optimize Ï€(a|s) directly. Which algorithm fits best?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "SARSA",
      "DQN"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE directly optimizes the policy.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm typically waits until returns are observed before applying an unbiased policy-gradient estimate?",
    "options": [
      "REINFORCE",
      "TD(0)",
      "A2C/A3C",
      "TD3"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE uses Monte Carlo returns for policy gradients.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which option is most appropriate when the action space is naturally stochastic and you want direct policy learning in an introductory setting?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE is a straightforward direct policy learner.",
    "category": "Policy Gradient"
  },
  {
    "question": "A professor writes âˆ‡Î¸ J(Î¸) â‰ˆ G_t âˆ‡Î¸ log Ï€Î¸(A_t|S_t). Which algorithm are they most likely teaching?",
    "options": [
      "REINFORCE",
      "PPO",
      "DDPG",
      "TD3"
    ],
    "answer": "REINFORCE",
    "explanation": "That is the classic REINFORCE form.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which method has high variance because it relies on sampled returns for policy gradients?",
    "options": [
      "REINFORCE",
      "TD(0)",
      "Q-learning",
      "DQN"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE gradients can be quite high variance.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm is often improved by adding a baseline to reduce variance while keeping the same basic policy-gradient idea?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "TD3",
      "SAC"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE commonly uses a baseline to reduce variance.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm is best described as 'policy gradient before actor-critic sophistication is added'?",
    "options": [
      "REINFORCE",
      "A2C/A3C",
      "PPO",
      "Actor-Critic"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE is the simpler Monte Carlo policy-gradient precursor.",
    "category": "Policy Gradient"
  },
  {
    "question": "If an exam asks for a direct policy-learning method that does not bootstrap by default, which answer is strongest?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "DQN",
      "TD(0)"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE is a direct non-bootstrapped policy-gradient method.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which method is conceptually easier than PPO for understanding basic stochastic policy gradients?",
    "options": [
      "REINFORCE",
      "PPO",
      "DDPG",
      "TD3"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE is the simpler foundational policy-gradient algorithm.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm updates action probabilities so that actions followed by high returns become more likely?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "DQN",
      "TRPO"
    ],
    "answer": "REINFORCE",
    "explanation": "That is the intuitive behavior of REINFORCE.",
    "category": "Policy Gradient"
  },
  {
    "question": "A tutorial says 'sample an episode, compute returns, then push up log-probabilities of good actions.' Which method is this?",
    "options": [
      "REINFORCE",
      "TD(0)",
      "Q-learning",
      "SAC"
    ],
    "answer": "REINFORCE",
    "explanation": "That is REINFORCE.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which method is often used to introduce why direct policy optimization can handle stochastic policies naturally?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "DQN",
      "DDPG"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE naturally models stochastic policies.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm family is REINFORCE part of?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "DQN",
      "TD(0)"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE is a policy-gradient method.",
    "category": "Policy Gradient"
  },
  {
    "question": "When value-based methods become awkward and you want parameterized stochastic actions, which simple foundational method is relevant?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "TD(0)",
      "SARSA"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE is the foundational direct policy approach.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm is more likely than Q-learning to be introduced when discussing gradients with respect to policy parameters?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "REINFORCE",
    "explanation": "Policy-parameter gradients point to REINFORCE.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which method best matches the phrase 'unbiased but high-variance policy gradient estimator'?",
    "options": [
      "REINFORCE",
      "PPO",
      "A2C/A3C",
      "DDPG"
    ],
    "answer": "REINFORCE",
    "explanation": "That classic description fits REINFORCE.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm is a natural first answer if a question asks about learning probabilities of actions directly from returns?",
    "options": [
      "REINFORCE",
      "Q-learning",
      "DQN",
      "TD(0)"
    ],
    "answer": "REINFORCE",
    "explanation": "REINFORCE does exactly that.",
    "category": "Policy Gradient"
  },
  {
    "question": "Which algorithm family combines a policy-learning actor with a value-estimating critic?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic combines policy and value learning.",
    "category": "Actor-Critic"
  },
  {
    "question": "A method uses one network to choose actions and another to evaluate them. Which family is this?",
    "options": [
      "Actor-Critic",
      "TD(0)",
      "Monte Carlo",
      "Q-learning"
    ],
    "answer": "Actor-Critic",
    "explanation": "That is the defining actor-critic architecture.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family is best seen as a bridge between pure policy gradients and TD learning?",
    "options": [
      "Actor-Critic",
      "REINFORCE",
      "DQN",
      "DDPG"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic uses a critic to stabilize policy learning.",
    "category": "Actor-Critic"
  },
  {
    "question": "A learner wants lower variance than REINFORCE by using a critic estimate. Which family should they choose?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "TD3",
      "DQN"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic reduces variance using a critic.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which option best matches 'policy update driven by an estimated advantage or TD error'?",
    "options": [
      "Actor-Critic",
      "Monte Carlo",
      "Q-learning",
      "TRPO"
    ],
    "answer": "Actor-Critic",
    "explanation": "That is a core actor-critic pattern.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family often updates the actor with gradients and the critic with a TD-style target?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "DQN",
      "SAC"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic naturally combines both update types.",
    "category": "Actor-Critic"
  },
  {
    "question": "If an exam asks for 'two-part architecture: action selector plus evaluator,' what should you answer?",
    "options": [
      "Actor-Critic",
      "TD(0)",
      "SARSA",
      "DDPG"
    ],
    "answer": "Actor-Critic",
    "explanation": "That phrase directly describes Actor-Critic.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family is more scalable to large problems than plain tabular SARSA or Q-learning?",
    "options": [
      "Actor-Critic",
      "SARSA",
      "Q-learning",
      "Monte Carlo"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic methods scale well with function approximation.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family commonly underlies many modern deep RL algorithms?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "TD(0)",
      "Monte Carlo"
    ],
    "answer": "Actor-Critic",
    "explanation": "Many modern methods are actor-critic variants.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which method family uses a critic to provide a learning signal that is usually less noisy than full-return REINFORCE?",
    "options": [
      "Actor-Critic",
      "REINFORCE",
      "TD3",
      "DDPG"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic reduces policy-gradient variance.",
    "category": "Actor-Critic"
  },
  {
    "question": "A student says, 'I want direct policy learning, but I also want a value function to guide it.' Which family fits?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "DQN",
      "TD(0)"
    ],
    "answer": "Actor-Critic",
    "explanation": "That is the central actor-critic idea.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family would you teach after REINFORCE to explain how a critic can improve training efficiency?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "DDPG",
      "TD3"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic is the natural next step after REINFORCE.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which option is the best general answer when both policy and value estimation are learned together?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "DQN",
      "Monte Carlo"
    ],
    "answer": "Actor-Critic",
    "explanation": "That is Actor-Critic.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family can naturally use TD errors as a signal for improving a stochastic policy?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "TD(0)",
      "DQN"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic commonly uses TD-based critics.",
    "category": "Actor-Critic"
  },
  {
    "question": "If the policy is parameterized continuously and you still want a value estimator, which broad family does that suggest?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "SARSA",
      "DQN"
    ],
    "answer": "Actor-Critic",
    "explanation": "That broad description points to Actor-Critic.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family contains A2C, A3C, PPO, SAC, DDPG, and TD3 as descendants or relatives?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "DQN",
      "Monte Carlo"
    ],
    "answer": "Actor-Critic",
    "explanation": "Those are all actor-critic style methods.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family is usually a better fit than REINFORCE when sample efficiency matters?",
    "options": [
      "Actor-Critic",
      "REINFORCE",
      "TD(0)",
      "Q-learning"
    ],
    "answer": "Actor-Critic",
    "explanation": "Actor-Critic is generally more sample-efficient.",
    "category": "Actor-Critic"
  },
  {
    "question": "A learning system has a policy network updated from advantage estimates and a value network updated from returns or TD targets. Which family is this?",
    "options": [
      "Actor-Critic",
      "Q-learning",
      "DQN",
      "TD3"
    ],
    "answer": "Actor-Critic",
    "explanation": "That is actor-critic structure.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which algorithm family is the advantage-based actor-critic variant commonly written as A2C or A3C?",
    "options": [
      "A2C/A3C",
      "Actor-Critic",
      "PPO",
      "REINFORCE"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C/A3C are advantage actor-critic methods.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which method improves on basic actor-critic by using an advantage estimate to reduce variance in policy updates?",
    "options": [
      "A2C/A3C",
      "Q-learning",
      "DQN",
      "DDPG"
    ],
    "answer": "A2C/A3C",
    "explanation": "That is the hallmark of A2C/A3C.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which algorithm is most associated with asynchronous parallel actor-learners in its classic form?",
    "options": [
      "A2C/A3C",
      "PPO",
      "TD3",
      "SAC"
    ],
    "answer": "A2C/A3C",
    "explanation": "A3C is the classic asynchronous advantage actor-critic.",
    "category": "Actor-Critic"
  },
  {
    "question": "A synchronous version of A3C is commonly called what?",
    "options": [
      "A2C/A3C",
      "Actor-Critic",
      "PPO",
      "Q-learning"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C is the synchronous counterpart.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which option best matches 'advantage actor-critic'?",
    "options": [
      "A2C/A3C",
      "TD(0)",
      "Q-learning",
      "DQN"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C/A3C literally stands for Advantage Actor-Critic.",
    "category": "Actor-Critic"
  },
  {
    "question": "A student wants a policy-gradient style method with a learned value baseline and often multiple workers. Which answer fits?",
    "options": [
      "A2C/A3C",
      "REINFORCE",
      "TRPO",
      "TD3"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C/A3C fit that description.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which algorithm commonly estimates A(s,a) rather than relying only on raw returns for policy updates?",
    "options": [
      "A2C/A3C",
      "Q-learning",
      "DQN",
      "DDPG"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C/A3C use an advantage estimate.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which method is historically important for showing that parallel actor-critic training can be practical and effective?",
    "options": [
      "A2C/A3C",
      "PPO",
      "TD3",
      "Q-learning"
    ],
    "answer": "A2C/A3C",
    "explanation": "That is a classic contribution of A3C.",
    "category": "Actor-Critic"
  },
  {
    "question": "When an exam asks for a deep RL actor-critic algorithm before PPO became the go-to standard, which answer is strong?",
    "options": [
      "A2C/A3C",
      "PPO",
      "DQN",
      "SAC"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C/A3C are classic earlier actor-critic methods.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which algorithm is a natural choice when you want a simpler actor-critic implementation than PPO but still with advantage estimates?",
    "options": [
      "A2C/A3C",
      "REINFORCE",
      "DDPG",
      "TD3"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C is often a simpler advantage actor-critic baseline.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family updates both a policy head and a value head while using advantage signals?",
    "options": [
      "A2C/A3C",
      "Q-learning",
      "Monte Carlo",
      "TD(0)"
    ],
    "answer": "A2C/A3C",
    "explanation": "That is A2C/A3C.",
    "category": "Actor-Critic"
  },
  {
    "question": "A learner mentions entropy bonus, value loss, and policy loss in one combined objective, in a classic actor-critic setting. Which algorithm family is likely?",
    "options": [
      "A2C/A3C",
      "DQN",
      "Q-learning",
      "TD3"
    ],
    "answer": "A2C/A3C",
    "explanation": "Those ingredients are common in A2C/A3C implementations.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which option best matches 'parallel workers collecting trajectories for advantage-based policy updates'?",
    "options": [
      "A2C/A3C",
      "TRPO",
      "SAC",
      "DDPG"
    ],
    "answer": "A2C/A3C",
    "explanation": "That points to A3C/A2C-style training.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which method would you mention if asked for a deep actor-critic algorithm suitable for discrete-action control with advantage estimation?",
    "options": [
      "A2C/A3C",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C/A3C are standard answers.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which algorithm stands between plain actor-critic and PPO in many course progressions?",
    "options": [
      "A2C/A3C",
      "Q-learning",
      "DQN",
      "TD(0)"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C/A3C often appear before PPO in course flow.",
    "category": "Actor-Critic"
  },
  {
    "question": "A quiz asks: 'Which algorithm family introduced asynchronous stabilization by many actor threads?'",
    "options": [
      "A2C/A3C",
      "PPO",
      "Q-learning",
      "TD3"
    ],
    "answer": "A2C/A3C",
    "explanation": "That is associated with A3C.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which method best fits the phrase 'advantage-based policy gradient with a critic baseline'?",
    "options": [
      "A2C/A3C",
      "REINFORCE",
      "Q-learning",
      "DQN"
    ],
    "answer": "A2C/A3C",
    "explanation": "That describes A2C/A3C.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which algorithm is usually easier to explain than PPO if the goal is just to grasp advantage actor-critic basics?",
    "options": [
      "A2C/A3C",
      "PPO",
      "SAC",
      "TD3"
    ],
    "answer": "A2C/A3C",
    "explanation": "A2C is the simpler stepping stone.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which family is particularly useful to know when studying how policy loss, value loss, and entropy regularization interact?",
    "options": [
      "A2C/A3C",
      "Q-learning",
      "DQN",
      "Monte Carlo"
    ],
    "answer": "A2C/A3C",
    "explanation": "Those are classic A2C/A3C training components.",
    "category": "Actor-Critic"
  },
  {
    "question": "Which algorithm is deep Q-learning with a neural network approximating action values?",
    "options": [
      "DQN",
      "Q-learning",
      "PPO",
      "DDPG"
    ],
    "answer": "DQN",
    "explanation": "DQN is Q-learning with a neural-network function approximator.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which method became famous for Atari game playing from pixels?",
    "options": [
      "DQN",
      "SAC",
      "TD3",
      "REINFORCE"
    ],
    "answer": "DQN",
    "explanation": "DQNâ€™s breakthrough results came from Atari.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm uses experience replay and a target network in its classic form?",
    "options": [
      "DQN",
      "Q-learning",
      "SARSA",
      "PPO"
    ],
    "answer": "DQN",
    "explanation": "Those are the classic DQN stabilizers.",
    "category": "Deep Value Methods"
  },
  {
    "question": "A learner has a large discrete action space and high-dimensional image observations. Which algorithm is a standard first deep RL choice?",
    "options": [
      "DQN",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "DQN",
    "explanation": "DQN is tailored to large state spaces with discrete actions.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm is inappropriate for truly continuous action spaces because it still relies on argmax over discrete actions?",
    "options": [
      "DQN",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "DQN",
    "explanation": "DQN is for discrete actions.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which method most directly inherits the max-backup idea from tabular Q-learning?",
    "options": [
      "DQN",
      "PPO",
      "REINFORCE",
      "Actor-Critic"
    ],
    "answer": "DQN",
    "explanation": "DQN is deep Q-learning.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm is best known for stabilizing off-policy value learning using replay memory?",
    "options": [
      "DQN",
      "A2C/A3C",
      "TRPO",
      "DDPG"
    ],
    "answer": "DQN",
    "explanation": "Replay memory is a central DQN feature.",
    "category": "Deep Value Methods"
  },
  {
    "question": "If an exam asks for the deep RL extension of Q-learning, what is the answer?",
    "options": [
      "DQN",
      "PPO",
      "SAC",
      "TD3"
    ],
    "answer": "DQN",
    "explanation": "That is DQN.",
    "category": "Deep Value Methods"
  },
  {
    "question": "A student says, 'My observations are images, my actions are left/right/jump, and I want a value-based deep method.' Which algorithm fits?",
    "options": [
      "DQN",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "DQN",
    "explanation": "Discrete actions plus image inputs are classic DQN territory.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which method uses a frozen or slowly updated target network to reduce training instability?",
    "options": [
      "DQN",
      "Q-learning",
      "TD(0)",
      "REINFORCE"
    ],
    "answer": "DQN",
    "explanation": "Target networks are a signature DQN trick.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm is more natural than PPO when actions are discrete and the goal is direct Q-value approximation from pixels?",
    "options": [
      "DQN",
      "PPO",
      "SAC",
      "DDPG"
    ],
    "answer": "DQN",
    "explanation": "That is the standard DQN use case.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm family commonly includes variants like Double DQN and Dueling DQN?",
    "options": [
      "DQN",
      "PPO",
      "TD3",
      "SAC"
    ],
    "answer": "DQN",
    "explanation": "Those are DQN variants.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which method is often less suitable than PPO for highly stochastic policy optimization but very natural for discrete action-values?",
    "options": [
      "DQN",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "DQN",
    "explanation": "DQN is an action-value method for discrete settings.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm would you pick before DDPG, TD3, or SAC when the action set is finite?",
    "options": [
      "DQN",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "DQN",
    "explanation": "DQN is the finite discrete-action choice.",
    "category": "Deep Value Methods"
  },
  {
    "question": "A learner wants off-policy reuse of past transitions in a large replay buffer. Which classic deep RL algorithm matches that idea?",
    "options": [
      "DQN",
      "A2C/A3C",
      "PPO",
      "REINFORCE"
    ],
    "answer": "DQN",
    "explanation": "Replay-buffer reuse is central to DQN.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which method is the best answer when you hear 'Q-network'?",
    "options": [
      "DQN",
      "Q-learning",
      "Actor-Critic",
      "PPO"
    ],
    "answer": "DQN",
    "explanation": "Q-network directly refers to DQN-style learning.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm is the natural deep baseline for CartPole, LunarLander, or Atari with discrete actions?",
    "options": [
      "DQN",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "DQN",
    "explanation": "Those are standard DQN benchmark types.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which method is associated with estimating Q(s,a; Î¸) using a neural network and then bootstrapping toward a max target?",
    "options": [
      "DQN",
      "PPO",
      "TD(0)",
      "REINFORCE"
    ],
    "answer": "DQN",
    "explanation": "That is DQN.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm is better suited than SAC for pixel-based games with a small finite action set?",
    "options": [
      "DQN",
      "SAC",
      "TD3",
      "DDPG"
    ],
    "answer": "DQN",
    "explanation": "DQN is usually the more natural choice in that setting.",
    "category": "Deep Value Methods"
  },
  {
    "question": "Which algorithm constrains policy updates using a trust-region idea based on KL divergence?",
    "options": [
      "TRPO",
      "PPO",
      "REINFORCE",
      "DQN"
    ],
    "answer": "TRPO",
    "explanation": "TRPO is Trust Region Policy Optimization.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which policy-optimization method is known for monotonic improvement motivations and constrained updates?",
    "options": [
      "TRPO",
      "PPO",
      "Q-learning",
      "TD3"
    ],
    "answer": "TRPO",
    "explanation": "TRPO is famous for trust-region constrained updates.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm came before PPO and inspired its stable-update philosophy?",
    "options": [
      "TRPO",
      "REINFORCE",
      "DDPG",
      "SAC"
    ],
    "answer": "TRPO",
    "explanation": "PPO is often presented as a simpler alternative to TRPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "A student says, 'I want a policy update that does not move too far in one step according to KL divergence.' Which algorithm are they describing?",
    "options": [
      "TRPO",
      "PPO",
      "Q-learning",
      "DQN"
    ],
    "answer": "TRPO",
    "explanation": "That is TRPOâ€™s central trust-region idea.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method is usually more mathematically involved than PPO because it solves a constrained optimization problem?",
    "options": [
      "TRPO",
      "PPO",
      "A2C/A3C",
      "DQN"
    ],
    "answer": "TRPO",
    "explanation": "TRPO is more mathematically complex than PPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is best identified by the word 'trust region' in its full name?",
    "options": [
      "TRPO",
      "PPO",
      "TD3",
      "DDPG"
    ],
    "answer": "TRPO",
    "explanation": "TRPO literally stands for Trust Region Policy Optimization.",
    "category": "Policy Optimization"
  },
  {
    "question": "If a question emphasizes KL-constrained step size rather than clipping, which answer is stronger?",
    "options": [
      "TRPO",
      "PPO",
      "SAC",
      "Actor-Critic"
    ],
    "answer": "TRPO",
    "explanation": "KL-constrained steps point to TRPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is an on-policy policy-gradient style method for stable updates, but is usually less convenient than PPO in practice?",
    "options": [
      "TRPO",
      "PPO",
      "DQN",
      "TD3"
    ],
    "answer": "TRPO",
    "explanation": "That description fits TRPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "A professor mentions conjugate gradient and Fisher-information style approximations in policy optimization. Which algorithm is likely being discussed?",
    "options": [
      "TRPO",
      "PPO",
      "Q-learning",
      "DQN"
    ],
    "answer": "TRPO",
    "explanation": "Those techniques are strongly associated with TRPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method aims to keep the new policy close to the old one within a trust region?",
    "options": [
      "TRPO",
      "PPO",
      "TD(0)",
      "Q-learning"
    ],
    "answer": "TRPO",
    "explanation": "That is the defining TRPO constraint.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is more likely than PPO to appear in a theory-heavy lecture on stable policy updates?",
    "options": [
      "TRPO",
      "PPO",
      "DDPG",
      "TD3"
    ],
    "answer": "TRPO",
    "explanation": "TRPO is more theory-heavy.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method would you cite if asked for a principled constrained policy-gradient algorithm?",
    "options": [
      "TRPO",
      "PPO",
      "Actor-Critic",
      "A2C/A3C"
    ],
    "answer": "TRPO",
    "explanation": "TRPO is the principled constrained approach.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is usually not the first practical choice for beginners because implementation is more involved?",
    "options": [
      "TRPO",
      "PPO",
      "DQN",
      "A2C/A3C"
    ],
    "answer": "TRPO",
    "explanation": "TRPO is harder to implement than PPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "If the exam stem includes 'optimize the surrogate objective under a KL-divergence constraint,' which algorithm should you choose?",
    "options": [
      "TRPO",
      "PPO",
      "DDPG",
      "SAC"
    ],
    "answer": "TRPO",
    "explanation": "That wording points to TRPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method is most associated with a trust-region rather than replay buffers or max Q backups?",
    "options": [
      "TRPO",
      "DQN",
      "Q-learning",
      "TD3"
    ],
    "answer": "TRPO",
    "explanation": "Trust-region policy constraints are TRPOâ€™s hallmark.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm usually requires more second-order optimization machinery than PPO?",
    "options": [
      "TRPO",
      "PPO",
      "REINFORCE",
      "Actor-Critic"
    ],
    "answer": "TRPO",
    "explanation": "TRPO uses more advanced optimization ideas.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which answer best matches 'stable but mathematically heavier policy optimization'?",
    "options": [
      "TRPO",
      "PPO",
      "Q-learning",
      "DQN"
    ],
    "answer": "TRPO",
    "explanation": "That is TRPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method is most directly connected to using KL divergence as a bound on policy change?",
    "options": [
      "TRPO",
      "PPO",
      "TD(0)",
      "DDPG"
    ],
    "answer": "TRPO",
    "explanation": "TRPO explicitly constrains KL change.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which policy-optimization algorithm stabilizes training with a clipped surrogate objective?",
    "options": [
      "PPO",
      "TRPO",
      "REINFORCE",
      "DQN"
    ],
    "answer": "PPO",
    "explanation": "PPO is known for clipping policy updates.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is often the practical go-to deep policy-gradient baseline because it is simpler than TRPO?",
    "options": [
      "PPO",
      "TRPO",
      "TD3",
      "DDPG"
    ],
    "answer": "PPO",
    "explanation": "PPO is popular because it is stable and relatively easy to implement.",
    "category": "Policy Optimization"
  },
  {
    "question": "A learner wants an on-policy actor-critic style method that works well in many environments without heavy trust-region machinery. Which algorithm fits?",
    "options": [
      "PPO",
      "TRPO",
      "Q-learning",
      "DQN"
    ],
    "answer": "PPO",
    "explanation": "That description matches PPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is more likely than DQN to be chosen for a modern project when stable policy optimization is desired across many tasks?",
    "options": [
      "PPO",
      "DQN",
      "Q-learning",
      "TD(0)"
    ],
    "answer": "PPO",
    "explanation": "PPO is a strong general-purpose policy-optimization method.",
    "category": "Policy Optimization"
  },
  {
    "question": "If a question mentions clipping the probability ratio between new and old policies, which algorithm is it?",
    "options": [
      "PPO",
      "TRPO",
      "REINFORCE",
      "Actor-Critic"
    ],
    "answer": "PPO",
    "explanation": "That is the PPO clipping mechanism.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is widely used for both discrete and continuous control with policy gradients?",
    "options": [
      "PPO",
      "DQN",
      "Q-learning",
      "TD3"
    ],
    "answer": "PPO",
    "explanation": "PPO handles both discrete and continuous action spaces.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method is usually easier to implement than TRPO but keeps the same goal of avoiding destructive policy jumps?",
    "options": [
      "PPO",
      "TRPO",
      "SAC",
      "DDPG"
    ],
    "answer": "PPO",
    "explanation": "PPO approximates stable updates with clipping.",
    "category": "Policy Optimization"
  },
  {
    "question": "A professor asks for the deep RL algorithm that uses clipped importance ratios in its objective. Which answer is correct?",
    "options": [
      "PPO",
      "REINFORCE",
      "Q-learning",
      "DQN"
    ],
    "answer": "PPO",
    "explanation": "That is PPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm would you likely try for Mario or Mujoco if you want a robust policy-gradient baseline?",
    "options": [
      "PPO",
      "DQN",
      "TD3",
      "SAC"
    ],
    "answer": "PPO",
    "explanation": "PPO is a very common strong baseline.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method is best described as an actor-critic style algorithm with minibatch optimization over collected trajectories?",
    "options": [
      "PPO",
      "Q-learning",
      "DQN",
      "TD(0)"
    ],
    "answer": "PPO",
    "explanation": "That is the standard PPO training pattern.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is generally on-policy, meaning it learns from freshly collected trajectories rather than a large replay buffer?",
    "options": [
      "PPO",
      "DQN",
      "TD3",
      "SAC"
    ],
    "answer": "PPO",
    "explanation": "PPO is fundamentally on-policy.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method is often chosen when DQN struggles with stability or when direct policy learning is preferred?",
    "options": [
      "PPO",
      "DQN",
      "Q-learning",
      "TD(0)"
    ],
    "answer": "PPO",
    "explanation": "PPO is a popular alternative for direct policy optimization.",
    "category": "Policy Optimization"
  },
  {
    "question": "If an exam stem says 'clip the objective so the new policy does not move too far from the old one,' which algorithm should stand out?",
    "options": [
      "PPO",
      "TRPO",
      "Actor-Critic",
      "A2C/A3C"
    ],
    "answer": "PPO",
    "explanation": "That is PPOâ€™s signature idea.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is the likely answer when the course discusses stable, simple, and popular policy-gradient optimization?",
    "options": [
      "PPO",
      "REINFORCE",
      "DDPG",
      "TD3"
    ],
    "answer": "PPO",
    "explanation": "That phrase strongly points to PPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method often uses advantage estimates together with a clipped policy loss and a value loss?",
    "options": [
      "PPO",
      "Q-learning",
      "DQN",
      "SAC"
    ],
    "answer": "PPO",
    "explanation": "Those ingredients define PPO training.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is commonly preferred over TRPO in practice because it is computationally simpler?",
    "options": [
      "PPO",
      "TRPO",
      "TD3",
      "DDPG"
    ],
    "answer": "PPO",
    "explanation": "PPO is the practical simplification.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which method is better suited than DQN when the action distribution needs to be parameterized directly?",
    "options": [
      "PPO",
      "DQN",
      "Q-learning",
      "TD(0)"
    ],
    "answer": "PPO",
    "explanation": "PPO directly parameterizes the policy.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm is an especially strong all-purpose baseline when you are unsure whether a more specialized continuous-control method is necessary?",
    "options": [
      "PPO",
      "DDPG",
      "TD3",
      "SAC"
    ],
    "answer": "PPO",
    "explanation": "PPO is a robust general-purpose baseline.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which answer best matches 'clipped surrogate, on-policy, actor-critic style deep RL'?",
    "options": [
      "PPO",
      "TRPO",
      "DQN",
      "Q-learning"
    ],
    "answer": "PPO",
    "explanation": "That is PPO.",
    "category": "Policy Optimization"
  },
  {
    "question": "Which algorithm applies actor-critic ideas to continuous actions using a deterministic policy?",
    "options": [
      "DDPG",
      "DQN",
      "PPO",
      "Q-learning"
    ],
    "answer": "DDPG",
    "explanation": "DDPG stands for Deep Deterministic Policy Gradient.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is a natural deep RL choice for continuous control before TD3 and SAC are considered?",
    "options": [
      "DDPG",
      "DQN",
      "PPO",
      "Q-learning"
    ],
    "answer": "DDPG",
    "explanation": "DDPG is a classic continuous-control baseline.",
    "category": "Continuous Control"
  },
  {
    "question": "A learner needs throttle and steering outputs that vary continuously. Which algorithm is a classic match?",
    "options": [
      "DDPG",
      "DQN",
      "TD(0)",
      "SARSA"
    ],
    "answer": "DDPG",
    "explanation": "Continuous action outputs fit DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm uses a deterministic actor and a critic trained off-policy with replay?",
    "options": [
      "DDPG",
      "PPO",
      "REINFORCE",
      "TRPO"
    ],
    "answer": "DDPG",
    "explanation": "That describes DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method can be viewed as an actor-critic continuous-action analogue of DQN-style off-policy learning?",
    "options": [
      "DDPG",
      "PPO",
      "Q-learning",
      "SAC"
    ],
    "answer": "DDPG",
    "explanation": "DDPG is often described that way.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is less appropriate than PPO when you specifically need stochastic policy robustness, but appropriate for deterministic continuous control?",
    "options": [
      "DDPG",
      "PPO",
      "DQN",
      "TD(0)"
    ],
    "answer": "DDPG",
    "explanation": "DDPG is deterministic and continuous-action focused.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method relies on deterministic policy gradients rather than sampling a full stochastic policy distribution?",
    "options": [
      "DDPG",
      "SAC",
      "PPO",
      "REINFORCE"
    ],
    "answer": "DDPG",
    "explanation": "That is DDPGâ€™s core idea.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm often needs exploration noise added externally because its actor is deterministic?",
    "options": [
      "DDPG",
      "SAC",
      "PPO",
      "TRPO"
    ],
    "answer": "DDPG",
    "explanation": "DDPG commonly adds OU or Gaussian noise for exploration.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is more fragile than TD3 and SAC but historically important for continuous control?",
    "options": [
      "DDPG",
      "TD3",
      "SAC",
      "PPO"
    ],
    "answer": "DDPG",
    "explanation": "DDPG is the earlier and less stable continuous-control actor-critic.",
    "category": "Continuous Control"
  },
  {
    "question": "If the action space is continuous and you want off-policy replay-based learning, which classic algorithm should come to mind?",
    "options": [
      "DDPG",
      "PPO",
      "DQN",
      "Q-learning"
    ],
    "answer": "DDPG",
    "explanation": "That is a standard DDPG use case.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is the correct answer when the stem says 'deep deterministic actor-critic'?",
    "options": [
      "DDPG",
      "TD3",
      "SAC",
      "A2C/A3C"
    ],
    "answer": "DDPG",
    "explanation": "That wording literally names DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method uses target networks for both actor and critic in a continuous-control setting?",
    "options": [
      "DDPG",
      "PPO",
      "TRPO",
      "REINFORCE"
    ],
    "answer": "DDPG",
    "explanation": "Target networks are standard in DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm would you likely replace with TD3 if overestimation and instability become major problems?",
    "options": [
      "DDPG",
      "DQN",
      "Q-learning",
      "TD(0)"
    ],
    "answer": "DDPG",
    "explanation": "TD3 was designed to improve DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is often associated with robotic arm control and other smooth motor outputs?",
    "options": [
      "DDPG",
      "DQN",
      "PPO",
      "Q-learning"
    ],
    "answer": "DDPG",
    "explanation": "Those are classic continuous-control applications.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm does not require discretizing the action space to choose among actions?",
    "options": [
      "DDPG",
      "DQN",
      "Q-learning",
      "SARSA"
    ],
    "answer": "DDPG",
    "explanation": "DDPG handles continuous actions directly.",
    "category": "Continuous Control"
  },
  {
    "question": "Which answer best matches 'off-policy actor-critic with deterministic actions and replay buffer'?",
    "options": [
      "DDPG",
      "PPO",
      "SAC",
      "TRPO"
    ],
    "answer": "DDPG",
    "explanation": "That description is DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method commonly uses the gradient of the critic with respect to the action to update the actor?",
    "options": [
      "DDPG",
      "PPO",
      "Q-learning",
      "DQN"
    ],
    "answer": "DDPG",
    "explanation": "That is the deterministic policy-gradient mechanism.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is more natural than DQN when the agent must output a real-valued control signal?",
    "options": [
      "DDPG",
      "DQN",
      "Q-learning",
      "TD(0)"
    ],
    "answer": "DDPG",
    "explanation": "DQN assumes discrete actions, while DDPG handles continuous control.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is the historical stepping stone from deterministic policy gradients to TD3?",
    "options": [
      "DDPG",
      "SAC",
      "PPO",
      "A2C/A3C"
    ],
    "answer": "DDPG",
    "explanation": "TD3 directly builds on DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm improves DDPG with twin critics and delayed policy updates?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "PPO"
    ],
    "answer": "TD3",
    "explanation": "TD3 stands for Twin Delayed DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is designed to reduce overestimation bias in continuous-control Q estimates?",
    "options": [
      "TD3",
      "DDPG",
      "DQN",
      "Q-learning"
    ],
    "answer": "TD3",
    "explanation": "Twin critics in TD3 help reduce overestimation.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is often preferred over plain DDPG because it is more stable in practice?",
    "options": [
      "TD3",
      "DDPG",
      "PPO",
      "REINFORCE"
    ],
    "answer": "TD3",
    "explanation": "TD3 fixes several DDPG instability issues.",
    "category": "Continuous Control"
  },
  {
    "question": "A learner mentions clipped double Q-learning ideas in a continuous deterministic actor-critic setting. Which algorithm is it?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "DQN"
    ],
    "answer": "TD3",
    "explanation": "That is TD3.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method delays actor updates relative to critic updates to improve stability?",
    "options": [
      "TD3",
      "DDPG",
      "PPO",
      "TRPO"
    ],
    "answer": "TD3",
    "explanation": "Delayed policy updates are a TD3 feature.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm adds target policy smoothing noise to the target action in continuous control?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "A2C/A3C"
    ],
    "answer": "TD3",
    "explanation": "Target policy smoothing is part of TD3.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method should come to mind when the exam mentions 'twin critics'?",
    "options": [
      "TD3",
      "DDPG",
      "PPO",
      "Q-learning"
    ],
    "answer": "TD3",
    "explanation": "Twin critics identify TD3.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is usually a stronger deterministic continuous-control baseline than DDPG?",
    "options": [
      "TD3",
      "DDPG",
      "DQN",
      "Q-learning"
    ],
    "answer": "TD3",
    "explanation": "TD3 is generally preferred to DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method remains deterministic in its actor design but corrects several weaknesses of DDPG?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "PPO"
    ],
    "answer": "TD3",
    "explanation": "That is TD3.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is best described as DDPG plus double critics, delayed updates, and target smoothing?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "TRPO"
    ],
    "answer": "TD3",
    "explanation": "Those are the defining TD3 improvements.",
    "category": "Continuous Control"
  },
  {
    "question": "If overestimation is hurting your continuous-control model, which algorithm is the most targeted fix?",
    "options": [
      "TD3",
      "DDPG",
      "PPO",
      "A2C/A3C"
    ],
    "answer": "TD3",
    "explanation": "TD3 was built for that problem.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is more specialized than PPO and usually chosen for continuous action spaces with deterministic control?",
    "options": [
      "TD3",
      "PPO",
      "DQN",
      "Q-learning"
    ],
    "answer": "TD3",
    "explanation": "TD3 is specialized continuous-control actor-critic.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm commonly outperforms DDPG by being less brittle during training?",
    "options": [
      "TD3",
      "DDPG",
      "REINFORCE",
      "TD(0)"
    ],
    "answer": "TD3",
    "explanation": "TD3 is the more robust successor.",
    "category": "Continuous Control"
  },
  {
    "question": "Which answer best matches 'continuous control, off-policy, deterministic actor, twin critics'?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "PPO"
    ],
    "answer": "TD3",
    "explanation": "That is TD3.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method would you likely choose instead of DDPG for Mujoco-style continuous benchmarks if you want better stability?",
    "options": [
      "TD3",
      "DDPG",
      "DQN",
      "Q-learning"
    ],
    "answer": "TD3",
    "explanation": "TD3 is a common upgrade over DDPG.",
    "category": "Continuous Control"
  },
  {
    "question": "A student says, 'My actor is deterministic, but my professor keeps talking about using the minimum of two critics.' Which algorithm is this?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "PPO"
    ],
    "answer": "TD3",
    "explanation": "Using the minimum of two critics is a TD3 hallmark.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is closer to DDPG than to SAC because it does not fundamentally rely on entropy maximization?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "PPO"
    ],
    "answer": "TD3",
    "explanation": "TD3 is a deterministic DDPG-style method, unlike SAC.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method often serves as a strong benchmark for low-dimensional continuous-control tasks?",
    "options": [
      "TD3",
      "DQN",
      "Q-learning",
      "Monte Carlo"
    ],
    "answer": "TD3",
    "explanation": "TD3 is a standard continuous-control benchmark.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is the natural answer when the stem includes the word 'Delayed' in a continuous actor-critic context?",
    "options": [
      "TD3",
      "DDPG",
      "SAC",
      "TRPO"
    ],
    "answer": "TD3",
    "explanation": "That word points to TD3.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm adds an entropy term to the objective to encourage exploration?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "DQN"
    ],
    "answer": "SAC",
    "explanation": "Soft Actor-Critic maximizes reward plus entropy.",
    "category": "Continuous Control"
  },
  {
    "question": "Which continuous-control algorithm is both off-policy and stochastic-policy based?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "PPO"
    ],
    "answer": "SAC",
    "explanation": "SAC learns a stochastic policy off-policy.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is often praised for strong performance and stability in continuous action spaces due to entropy regularization?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "Q-learning"
    ],
    "answer": "SAC",
    "explanation": "That description fits SAC.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm would you likely prefer over DDPG when you want richer exploration and a stochastic actor?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "DQN"
    ],
    "answer": "SAC",
    "explanation": "SAC uses entropy to encourage exploration.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is associated with the phrase 'maximum entropy reinforcement learning'?",
    "options": [
      "SAC",
      "PPO",
      "TRPO",
      "Q-learning"
    ],
    "answer": "SAC",
    "explanation": "That is the core idea behind SAC.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm uses a stochastic policy but still trains off-policy with replay buffers?",
    "options": [
      "SAC",
      "PPO",
      "REINFORCE",
      "A2C/A3C"
    ],
    "answer": "SAC",
    "explanation": "That combination is characteristic of SAC.",
    "category": "Continuous Control"
  },
  {
    "question": "A student says, 'I want continuous control, strong exploration, and a modern robust baseline.' Which algorithm fits best?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "DQN"
    ],
    "answer": "SAC",
    "explanation": "SAC is a strong modern continuous-control baseline.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is more exploratory than TD3 because it explicitly encourages policy entropy?",
    "options": [
      "SAC",
      "TD3",
      "DDPG",
      "PPO"
    ],
    "answer": "SAC",
    "explanation": "Entropy regularization gives SAC stronger exploration.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is a good answer when the policy distribution may be Gaussian and actions are continuous?",
    "options": [
      "SAC",
      "DQN",
      "Q-learning",
      "TD(0)"
    ],
    "answer": "SAC",
    "explanation": "SAC commonly parameterizes Gaussian continuous-action policies.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method optimizes both expected return and randomness of the policy?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "Q-learning"
    ],
    "answer": "SAC",
    "explanation": "That is the defining SAC objective.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is often preferred in hard continuous-control tasks where deterministic methods explore poorly?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "DQN"
    ],
    "answer": "SAC",
    "explanation": "SACâ€™s entropy objective improves exploration.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is best described as a stochastic actor-critic counterpart to deterministic continuous-control methods?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "PPO"
    ],
    "answer": "SAC",
    "explanation": "SAC is the stochastic off-policy continuous-control actor-critic.",
    "category": "Continuous Control"
  },
  {
    "question": "If an exam mentions temperature Î± controlling the entropy tradeoff, which algorithm should stand out?",
    "options": [
      "SAC",
      "PPO",
      "Q-learning",
      "DQN"
    ],
    "answer": "SAC",
    "explanation": "The entropy temperature is a standard SAC concept.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm often uses twin critics like TD3 but differs by optimizing a maximum-entropy objective?",
    "options": [
      "SAC",
      "DDPG",
      "PPO",
      "TRPO"
    ],
    "answer": "SAC",
    "explanation": "That is SAC.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is more natural than DQN when the agent must output a continuous action distribution?",
    "options": [
      "SAC",
      "DQN",
      "Q-learning",
      "SARSA"
    ],
    "answer": "SAC",
    "explanation": "DQN is discrete-action only; SAC handles continuous distributions.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is especially appropriate if you want a strong modern benchmark for robotics and locomotion tasks?",
    "options": [
      "SAC",
      "TD(0)",
      "Monte Carlo",
      "Q-learning"
    ],
    "answer": "SAC",
    "explanation": "SAC is widely used for such continuous-control benchmarks.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method can be thought of as off-policy actor-critic plus entropy maximization?",
    "options": [
      "SAC",
      "A2C/A3C",
      "REINFORCE",
      "DQN"
    ],
    "answer": "SAC",
    "explanation": "That summarizes SAC well.",
    "category": "Continuous Control"
  },
  {
    "question": "Which algorithm is a likely answer when the course asks about why entropy can prevent premature convergence to narrow policies?",
    "options": [
      "SAC",
      "DDPG",
      "TD3",
      "PPO"
    ],
    "answer": "SAC",
    "explanation": "SAC explicitly uses entropy to avoid overly narrow policies.",
    "category": "Continuous Control"
  },
  {
    "question": "Which method is usually stronger than DDPG when exploration quality is a major concern?",
    "options": [
      "SAC",
      "DDPG",
      "DQN",
      "Q-learning"
    ],
    "answer": "SAC",
    "explanation": "SAC typically explores more effectively.",
    "category": "Continuous Control"
  }
]

ALGO_GUIDE = {
  "Monte Carlo": "Learns from complete episodes. Best when episodes end clearly and you can wait for the final return.",
  "TD(0)": "One-step temporal-difference learning. Updates online with reward plus next-state estimate.",
  "TD(n)": "Uses an n-step return before bootstrapping. A middle ground between TD(0) and Monte Carlo.",
  "TD(λ)": "Blends many n-step returns using eligibility traces. Bridges TD(0) and Monte Carlo.",
  "SARSA": "On-policy TD control. Updates from the action actually taken next.",
  "SARSA(λ)": "SARSA plus eligibility traces for faster on-policy credit assignment.",
  "Q-learning": "Off-policy TD control. Uses the greedy max over next actions.",
  "REINFORCE": "Monte Carlo policy gradient. Learns the policy directly from sampled returns.",
  "Actor-Critic": "Actor chooses actions; critic evaluates them. Combines policy and value learning.",
  "A2C/A3C": "Advantage Actor-Critic methods. Often easier and more stable than plain REINFORCE.",
  "DQN": "Deep Q-learning for large state spaces with discrete actions.",
  "TRPO": "Trust-region policy optimization. Stable but more mathematically involved.",
  "PPO": "Clipped policy optimization. Popular, stable, and practical for many tasks.",
  "DDPG": "Off-policy deterministic actor-critic for continuous actions.",
  "TD3": "Improved DDPG with twin critics and delayed updates.",
  "SAC": "Off-policy stochastic actor-critic with entropy regularization for strong exploration."
}

ALGO_ORDER = list(ALGO_GUIDE.keys())

def get_default_batch():
    return 50

def algorithm_counts(question_bank):
    return Counter(q["answer"] for q in question_bank)

def build_new_batch(batch_size=50):
    pool = QUESTIONS[:]
    random.shuffle(pool)

    # Balanced sampling where possible
    grouped = {}
    for q in pool:
        grouped.setdefault(q["answer"], []).append(q)

    batch = []
    base_take = batch_size // len(ALGO_ORDER)
    remainder = batch_size % len(ALGO_ORDER)

    for algo in ALGO_ORDER:
        take = min(base_take, len(grouped.get(algo, [])))
        batch.extend(grouped.get(algo, [])[:take])

    leftovers = []
    for algo in ALGO_ORDER:
        leftovers.extend(grouped.get(algo, [])[base_take:])

    random.shuffle(leftovers)
    while len(batch) < batch_size and leftovers:
        batch.append(leftovers.pop())

    random.shuffle(batch)
    return batch

def initialize_state():
    if "quiz_questions" not in st.session_state:
        st.session_state.quiz_questions = build_new_batch(get_default_batch())
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "submitted" not in st.session_state:
        st.session_state.submitted = False
    if "score" not in st.session_state:
        st.session_state.score = 0
    if "missed" not in st.session_state:
        st.session_state.missed = []
    if "show_guide" not in st.session_state:
        st.session_state.show_guide = False

def reset_quiz():
    st.session_state.quiz_questions = build_new_batch(get_default_batch())
    st.session_state.answers = {}
    st.session_state.submitted = False
    st.session_state.score = 0
    st.session_state.missed = []

initialize_state()

with st.sidebar:
    st.title("RL Course Practice")
    st.write("Use this app for quiz practice and review while learning the course material.")
    st.write("**Question bank:** 300 true unique questions")
    st.write("**Batch size:** 50 shuffled questions per quiz")
    counts = algorithm_counts(QUESTIONS)
    st.write("**Coverage by algorithm**")
    for algo in ALGO_ORDER:
        st.caption(f"{algo}: {counts.get(algo, 0)}")
    if st.button("Start New 50-Question Quiz", use_container_width=True):
        reset_quiz()
        st.rerun()

st.title("Reinforcement Learning Course Practice Dashboard")
st.write("Use this for **practice, review, and repetition** so the major RL algorithms become easier to recognize and compare.")

tab1, tab2, tab3 = st.tabs(["Quiz", "Study Guide", "Missed Questions"])

with tab1:
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        st.metric("Questions This Quiz", len(st.session_state.quiz_questions))
    with col2:
        answered_count = sum(1 for i in range(len(st.session_state.quiz_questions)) if f"q_{i}" in st.session_state)
        st.metric("Answered So Far", answered_count)
    with col3:
        st.metric("Question Bank Size", len(QUESTIONS))

    st.info("Tip: Before answering, ask yourself three things: **episodic or ongoing? discrete or continuous actions? value-based or policy-based?**")

    for i, q in enumerate(st.session_state.quiz_questions):
        st.markdown(f"### Question {i+1}")
        user_choice = st.radio(
            q["question"],
            q["options"],
            key=f"q_{i}",
            index=None,
            disabled=st.session_state.submitted
        )
        if st.session_state.submitted:
            if user_choice == q["answer"]:
                st.success(f"Correct: {q['answer']}")
            else:
                st.error(f"Your answer: {user_choice if user_choice else 'No answer'}")
                st.write(f"**Correct answer:** {q['answer']}")
            st.write(f"**Why:** {q['explanation']}")
            st.caption(f"Algorithm focus: {q['answer']}")
        st.write("")

    submit_col1, submit_col2 = st.columns([1,1])
    with submit_col1:
        if st.button("Submit Quiz", type="primary", use_container_width=True, disabled=st.session_state.submitted):
            score = 0
            missed = []
            answers = {}
            for i, q in enumerate(st.session_state.quiz_questions):
                user_choice = st.session_state.get(f"q_{i}")
                answers[i] = user_choice
                if user_choice == q["answer"]:
                    score += 1
                else:
                    missed.append({**q, "your_answer": user_choice})
            st.session_state.answers = answers
            st.session_state.score = score
            st.session_state.missed = missed
            st.session_state.submitted = True
            st.rerun()
    with submit_col2:
        if st.button("Reset This Quiz", use_container_width=True):
            for i in range(len(st.session_state.quiz_questions)):
                key = f"q_{i}"
                if key in st.session_state:
                    del st.session_state[key]
            st.session_state.answers = {}
            st.session_state.submitted = False
            st.session_state.score = 0
            st.session_state.missed = []
            st.rerun()

    if st.session_state.submitted:
        st.divider()
        st.subheader("Quiz Result")
        st.write(f"**Score:** {st.session_state.score} / {len(st.session_state.quiz_questions)}")
        percent = 100 * st.session_state.score / len(st.session_state.quiz_questions)
        st.progress(percent / 100)
        if percent >= 85:
            st.success("Excellent. You're recognizing algorithm fit very well.")
        elif percent >= 70:
            st.info("Good progress. Review the missed questions to strengthen the weak spots.")
        else:
            st.warning("You're learning. Focus on the study guide and especially the missed-question review.")

        missed_by_algo = Counter(q["answer"] for q in st.session_state.missed)
        if missed_by_algo:
            st.write("**Algorithms to revisit most:**")
            for algo, n in missed_by_algo.most_common(5):
                st.write(f"- {algo}: {n} missed")
        else:
            st.write("Perfect score - no missed questions.")

with tab2:
    st.subheader("Study Guide: How to Tell the Algorithms Apart")
    st.write("Read this before or after a quiz. The goal is to connect each algorithm to its **learning style, action space, and use case**.")

    for algo in ALGO_ORDER:
        with st.expander(algo, expanded=False):
            st.write(ALGO_GUIDE[algo])
            if algo == "Monte Carlo":
                st.write("**Use when:** episodes end clearly and you can wait for the final return.")
                st.write("**Watch for:** higher variance, slower online feedback.")
            elif algo == "TD(0)":
                st.write("**Use when:** you need online updates after each step.")
                st.write("**Watch for:** one-step bootstrapping bias.")
            elif algo == "TD(n)":
                st.write("**Use when:** TD(0) feels too short-sighted but full Monte Carlo is too delayed.")
                st.write("**Watch for:** choosing n to balance bias and variance.")
            elif algo == "TD(λ)":
                st.write("**Use when:** you want richer credit assignment with eligibility traces.")
                st.write("**Watch for:** understanding lambda, forward view, and backward view.")
            elif algo == "SARSA":
                st.write("**Use when:** you want on-policy control and want learning to reflect exploratory behavior.")
                st.write("**Watch for:** safer behavior in tasks like cliff walking.")
            elif algo == "SARSA(λ)":
                st.write("**Use when:** you want SARSA plus faster reward propagation through traces.")
                st.write("**Watch for:** same on-policy logic, but with lambda tuning.")
            elif algo == "Q-learning":
                st.write("**Use when:** actions are discrete and you want off-policy control toward the greedy optimum.")
                st.write("**Watch for:** aggressive behavior because it assumes best future action.")
            elif algo == "REINFORCE":
                st.write("**Use when:** you want direct policy learning and a simple policy-gradient baseline.")
                st.write("**Watch for:** high variance unless you add a baseline.")
            elif algo == "Actor-Critic":
                st.write("**Use when:** you want direct policy learning guided by a value estimate.")
                st.write("**Watch for:** keeping actor and critic training balanced.")
            elif algo == "A2C/A3C":
                st.write("**Use when:** you want a practical advantage actor-critic baseline.")
                st.write("**Watch for:** policy loss, value loss, and entropy terms.")
            elif algo == "DQN":
                st.write("**Use when:** state space is large but action space is discrete.")
                st.write("**Watch for:** replay buffer, target network, and discrete actions only.")
            elif algo == "TRPO":
                st.write("**Use when:** you need trust-region style stable policy updates and care about theory.")
                st.write("**Watch for:** KL constraints and more complex optimization.")
            elif algo == "PPO":
                st.write("**Use when:** you want a strong, practical deep RL baseline.")
                st.write("**Watch for:** clipping, on-policy data collection, and advantage estimates.")
            elif algo == "DDPG":
                st.write("**Use when:** actions are continuous and deterministic control is acceptable.")
                st.write("**Watch for:** exploration noise and instability compared with TD3/SAC.")
            elif algo == "TD3":
                st.write("**Use when:** DDPG is unstable and you still want deterministic continuous control.")
                st.write("**Watch for:** twin critics, delayed policy updates, and target smoothing.")
            elif algo == "SAC":
                st.write("**Use when:** actions are continuous and you want strong exploration with a stochastic policy.")
                st.write("**Watch for:** entropy regularization and temperature tuning.")

with tab3:
    st.subheader("Missed Question Review")
    if not st.session_state.submitted:
        st.write("Submit a quiz first to populate this review tab.")
    elif not st.session_state.missed:
        st.success("No missed questions in the last quiz.")
    else:
        st.write(f"You missed **{len(st.session_state.missed)}** question(s). Review them carefully.")
        for idx, q in enumerate(st.session_state.missed, start=1):
            st.markdown(f"### Missed {idx}")
            st.write(q["question"])
            st.write(f"**Your answer:** {q['your_answer'] if q['your_answer'] else 'No answer'}")
            st.write(f"**Correct answer:** {q['answer']}")
            st.write(f"**Why:** {q['explanation']}")
            st.caption(f"Algorithm focus: {q['answer']}")
            st.write("")

st.caption("Built for course practice: each quiz uses a newly shuffled batch of questions.")

