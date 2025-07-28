-- priority and severty statistic
SELECT 
    p.pname AS priority,
    s.pname AS status,
    COUNT(i.id) AS bug_count,
    ROUND(AVG(EXTRACT(EPOCH FROM (NOW() - i.created)/86400))) AS avg_age_days
FROM jiraissue i
JOIN priority p ON i.priority = p.id
JOIN issuestatus s ON i.issuestatus = s.id
JOIN issuetype t ON i.issuetype = t.id
WHERE t.pname = 'Bug'
GROUP BY p.pname, s.pname
ORDER BY bug_count DESC;