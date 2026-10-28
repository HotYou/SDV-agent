# Stardew Valley Multi-Agent Project

The dream: a team of AI agents that play Stardew Valley together, just like a group of human players. No game mods, no C#, just Python.

## The plan

1. **Hands**: Scripts that press keys in the game. (Done! A script watered a crop.)
2. **Eyes**: Screenshots and pixel colors. For example, the agent can tell dry soil from watered soil.
3. **Brain**: Simple rules first: water if dry, skip if wet. Then the agent learns from its experience: it watches what happens after each action, and uses that to decide better next time.
4. **A team of agents**: Farming, fishing, mining, and combat agents working together on one farm, plus managing agents (when the team grows) that coordinate the team.

## Current status

Step 1 is done: the agent watered a crop in Stardew Valley. It uses `pydirectinput`, because the game ignores `pyautogui`'s keyboard and mouse input.

## The first agent

This is the first agent that is learning how to farm. It can already water a crop. Next, it will learn to water a whole field by itself. The goal is for it to use AI to decide for itself, not just follow a preprogrammed rule.

## Playing together

The agents play in co-op mode on one farm, with shared money. Since money is shared, spending is a team decision: the agents communicate with each other in the in-game chat box about spending priorities and quest completion planning. When the team grows, managing agents coordinate the team. The agents also participate in the storyline: gaining friendships with the villagers, attending festivals, revitalizing the village, not just doing chores.

## Talking with the agents

Agents communicate through the in-game chat, just like human players. Humans can talk to them there too, and they can reply the same way. They start with a shared command board and simple keywords; as their eyes and brains improve, they will understand natural language.

## Why this way?

Real players use eyes and hands. If agents learn to play through the screen and keyboard, they can play any game, not just one with a modding API. They will be excellent gaming companions for humans.

## Contributing
Any input is welcome!

## Next step
Let the agent see the soil and correctly decide whether it needs watering.
