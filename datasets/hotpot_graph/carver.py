#!/usr/bin/env python3

import json

markdown = """
# All Questions and Answers


"""

j = json.load(open("dev_graph_filtered.json"))

for each in j["all_questions"]:
    question = each["question"]
    answers = [node["full_name"] for node in each["node"]]
    # print(answers)

    markdown += "> " + question + "\n\n"
    for answer in answers:
        # "full_name" can have multiple fields, so we add them all in
        markdown += "* " + "\n    - ".join(answer) + "\n"
    markdown += "\n\n"

with open("all_info.md", "w") as filp:
    filp.write(markdown)
