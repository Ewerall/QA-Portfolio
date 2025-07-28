-- how long issue doesnt touch
SELECT 
    p.pkey || '-' || i.issuenum AS issue_key,
    i.summary,
    u.display_name AS assignee,
    i.created AS created_date,
    i.updated AS last_updated,
    EXTRACT(EPOCH FROM (NOW() - i.updated))/86400 AS days_inactive
FROM jiraissue i
JOIN project p ON i.project = p.id
LEFT JOIN cwd_user u ON i.assignee = u.user_name
WHERE i.resolution IS NULL
ORDER BY days_inactive DESC
LIMIT 20;