terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  profile = "my-second-profile"  # Profile should be a string
  region  = "us-east-1"
}


