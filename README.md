Python module for extracting DoD Small Business Innovation Research (SBIR) topics from http://dodsbir.net

#### Extracted topic fields

```
program
topic_number
title
areas
url
acquisition_program
objective
description
phases
references
keywords
solicitation_id
pre_release_date
proposals_begin_date
proposals_end_date
particpating_components
```

## Examples

#### Get list of topic numbers and solicitation information
```python
from dodsbirscrape import DODSBIRScrape

#initialize
s = DODSBIRScrape()

#get current solicitation information including list of topics
s.stage_current_solicitation()

#see what was grabbed
print s.topic_ids
print s.solicitation_id

```

#### Get topic from topic number
```python
from dodsbirscrape import DODSBIRScrape

#initialize
s = DODSBIRScrape()

#get a topic based on topic number
topic = s.get_topic("SB142-004")

#see what you grabbed
print topic.title
print topic.solicitation_id
print topic.description

```

#### Get all topics and save as a JSON file
```python
from dodsbirscrape import DODSBIRScrape

s = DODSBIRScrape()
s.stage_current_solicitation()
s.get_all_topics() #takes one second per topic (roughly 90 seconds total)
s.save_as_json() #saves to alltopics.json by default

```

## Bugs and Limitations

- The scraper doesn't retrieve questions and answers associated with topics.
