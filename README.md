# Vendori Backend Async

A few years ago I decided to write a web application to help my wife manage her team of bloggers for her Second Life in-world store.

## The Problem

Brands maintain a healthy relationship with bloggers in Second Life. Bloggers have access to some of the products a brand sells in Second Life, for free, in exchange for some free publicity by either reviewing the product or by designing a space or a look using featuring these products. With too many products and too many blogs, brand owners have trouble ensuring they have shared the new products with all their bloggers as well as if the bloggers are actually using them and how. Doing it manually is time-consuming and prevent them from spending time actually building and maintaining a good relationship with the bloggers.

## The Solution

Vendori needs to provide a web application where brand owners can create accounts for them, invite their blogger teams, and publish products they want bloggers to use. Vendori takes care of showing the list of available products to bloggers and delivering these products to them, upon request, directly in Second Life. Vendori also allows bloggers to share links to blog posts or videos they created and tag which products from which brands were used. This helps brands see if they have inactive bloggers, as well as to approve/reject content from bloggers if that's part of their agreement. Lastly, it might control quotas for bloggers, not allowing them to get more than N products before sharing content about the products they already got.

## Life span

The actual application was live for about 1 year. During this time, we operated with a few paying brands in beta mode. Ultimately I decided to shut down the experiment. This repository is not the actual code base, but a second take on the problem. The original app was written in Django using a custom flavor of [Django API Domains](https://github.com/phalt/django-api-domains). This one now incorporates other ideas, like FastAPI and asyncio, better dependency injection and clean architecture / ports and adapters concepts.
