# Urban Decay Roguelike - Development Roadmap

## Core Features
- [ ] Procedural dungeon generation for 6 levels
- [x] Stairs implementation and level progression
- [ ] Combat system with stat calculations (HP/AC/DM)
- [ ] Enemy AI and behaviors
- [ ] XP system and level progression
- [ ] Win/lose conditions

## Entity System
- [ ] Player stats implementation (LVL, HP, ST, DX, XP)
- [ ] Enemy types (Rats, Scavengers, Corrupted Officials)
- [ ] Item system (weapons, armor, heals, caps)
  - **Weapons**:
    - Pipe Wrench (`)`)
    - Baseball Bat (`/`)
    - Fire Axe (`†`)
  - **Armor**:
    - Leather Jacket (`[`)
    - Police Vest (`]`)
    - Hard Hat (`^`)
  - **Consumables**:
    - First-Aid Kit (`!`)
    - Painkillers (`+`)
    - Clean Water (`~`)
  - **Currency**: Bottle Caps (`$`)
- [ ] Inventory management
- [ ] Equipment system

## UI & UX
- [ ] Complete player stats panel
- [ ] Implement health bars for enemies
- [ ] Improve message log with message types (combat, system, etc.)

## Procedural Generation
- [ ] Implement cellular automata for organic maps
- [ ] Add BSP trees for room placement
- [ ] Create level-specific tilesets for each level
- [ ] Implement item/enemy placement algorithms

## Polish & Optimization
- [ ] Balance enemy stats and item values
- [ ] Add sound effects and background music
- [ ] Implement screen transitions
- [ ] Create victory/defeat screens

## Technical Debt
- [ ] Implement proper entity-component-system architecture
- [ ] Create automated tests for core mechanics
- [ ] Improve error handling and logging

## Content Creation
- [ ] Design 6 unique level themes:
  1. Street Level (Crumbling houses and overgrown streets)
  2. Abandoned Downtown (Collapsed storefronts and office buildings)
  3. Subway System (Collapsed tunnels)
  4. Sewer Network (Flooded passages)
  5. Industrial District (Derelict factories and warehouses)
  6. Central Bunker (Final challenge, Mayor's emergency shelter)
- [ ] Create enemy variants for each level
  - Level 1: Rodents, Scavengers
  - Level 2: Scavengers, ???
  - Level 3: Rodents, ???
  - Level 4: ???, Corrupt Officials
  - Level 5: Wild Animals, Corrupt Officials
  - Level 6: Elite Guards, Mayor (final challenge)
- [ ] Design thematic items for each level:
  - Suburbs: Baseball bat, garden tools
  - Downtown: Cash register money, jewelry
  - Sewers: Makeshift raft, water filter
  - Industrial: Hard hat, steel-toe boots
  - Storage: Canned food, bottled water
  - Bunker: Military gear, encrypted files
- [ ] Write lore snippets for world-building
  - [ ] Environmental storytelling through debris:
    - Foreclosure notices
    - Protest signs
    - Abandoned possessions
  - [ ] Audio logs from former residents
  - [ ] Newspaper fragments about economic collapse
  - [ ] Mayor's final orders in bunker terminal

## World-Building Details
- Economic collapse caused by:
  - Factory closures
  - Banking crisis
- Society breakdown:
  - Looting and scavenging
  - Formation of gangs
  - Last government remnants in bunker
- Environmental decay:
  - Nature reclaiming urban areas
  - Infrastructure collapse
  - Contaminated water sources

## Release Preparation
- [ ] Create game icon and splash screen
- [ ] Implement settings menu (volume, controls)
- [ ] Build executable with PyInstaller
- [ ] Create installation package

---

## Current Progress (Phase 1)
- [x] Pygame window setup
- [x] Character-based rendering system
- [x] Player movement with collision detection
- [x] Basic map generation from text templates
- [x] UI layout with message log and stats panel
- [x] Fonts for map and UI
- [x] Message wrapping and log management

## Phase 2 Goals
- [ ] Implement procedural level generation
- [x] Create entity system with base classes
- [x] Add first enemy type (Scavenger)
- [x] Implement basic combat mechanics
- [x] Create stairs for level progression
