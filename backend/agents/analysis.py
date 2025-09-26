import statistics

def analyze_performance(details, times):
    topic_stats = {}
    for d, t in zip(details, times):
        topic_stats.setdefault(d['topic'], {'correct':0,'total':0,'times':[]})
        topic_stats[d['topic']]['correct'] += d['correct']
        topic_stats[d['topic']]['total'] += 1
        topic_stats[d['topic']]['times'].append(t)

    report = []
    for topic, vals in topic_stats.items():
        avg_time = round(statistics.mean(vals['times']), 2)
        accuracy = round((vals['correct']/vals['total']) * 100, 2)
        report.append({"topic":topic, "accuracy":accuracy, "avg_time_sec":avg_time})
    return report
