# Flask docker app
Sample Flask app to run in a Docker container.

CodePipeline:
1. Source GitHub repository, watching for PUSH events
2. Trigger CodeBuild job from CodePipeline - builds Docker image and pushes to local ECR
3. Await manual approval after successful execution of CodeBuild job
4. Productionize by copying latest Docker image from local ECR to foreign prod ECR by assuming a foreign role
5. TODO: add `kubectl rollout restart` in prod automation to refresh pods with new, updated image
