-- issue status
SELECT p.pkey AS project_key, 
       ist.pname AS status,
       COUNT(i.id) AS issues_count
FROM jiraissue i
JOIN project p ON i.project = p.id
JOIN issuestatus ist ON i.issuestatus = ist.id
GROUP BY p.pkey, ist.pname
ORDER BY project_key, issues_count DESC;

-- opened issue > 7 days
SELECT i.id, p.pkey||'-'||i.issuenum AS issue_key, i.summary
FROM jiraissue i
JOIN project p ON i.project = p.id
WHERE i.updated < NOW() - INTERVAL '7 days'
AND i.resolution IS NULL;