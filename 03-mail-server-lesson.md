# Lesson 2 (skeleton) — Mail server: set up James, create her account

**Objective.** Understand how the Apache James mail server runs on Lampy,
and finish the lesson holding a working mailbox of your own:
`gwen@localhost`. This is real work — the account you create here is the
administrator identity you will use from now on.

## Questions to answer from your approved sources

1. What is Apache James, and what does it do on the Lampy stack?
2. How does this James installation store its users? (Hint: check how the
   container's James is configured — its config files are part of your
   evidence.)
3. What is the WebAdmin API, and how do you add a user with it?
4. What domain does Lampy's James serve? Where is that configured?

Approved sources for this lesson: the official James documentation at
https://james.apache.org/ and your Debian Administrator's Handbook
(mail server chapters). Look the procedures up yourself.

## Hands-on tasks

1. Confirm James is running and healthy (healthcheck).
2. Read the domain configuration and state the domain in your report.
3. Create your mailbox `gwen@localhost` through the WebAdmin API,
   using the password Kit chose. (Muse will hand you the password at
   execution time — it is not written in your files.)
4. Verify the account exists and report the evidence.

## Done when

You can send mail as `gwen@localhost`, and your report quotes the evidence
for each step: healthcheck output, domain config, user-creation response.
