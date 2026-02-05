---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
draft: false
type: "meeting"
meeting_type: "technical"  # technical or nomikai
location: ""
venue: ""
address: ""
map_url: ""
start_time: "19:00"
categories: ["meetings"]
tags: []
years: ["{{ dateFormat "2006" .Date }}"]
meeting-types: ["technical"]
description: ""
---

## Meeting Details

**Date:** {{ dateFormat "Monday, January 2, 2006" .Date }}  
**Time:** 19:00 - 21:00  
**Location:** TBD  
**Venue:** TBD  

## Presentations

### Main Presentation

**Speaker:** TBD  
**Topic:** TBD  

Description of the presentation...

### Lightning Talks

- **Speaker Name** - Topic

## After-party (Nomikai)

After the meeting, we'll gather at a nearby restaurant for food and drinks.

**Location:** TBD  
**Time:** Approximately 21:00  

## Getting There

Directions to the venue...

## About TLUG Meetings

TLUG meetings are open to everyone. You don't need to be a Linux expert to attend!
