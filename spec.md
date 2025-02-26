# Link Inbox App Specification

## Overview
A Flask-based application for storing and managing interesting links, with a simple two-page interface for adding and viewing links.

## Core Features

### Data Structure
- Database: SQLite (for Datasette compatibility)
- Required fields:
  - URL (validated)
  - Why Interesting (text)
  - Notes (optional text)
  - Creation Date (timestamp, auto-generated)

### Pages

1. Input Page:
   - Simple form with three fields:
     - URL (required, with validation)
     - Why Interesting (required)
     - Notes (optional)
   - Submit button
   - Navigation to view page

2. View Page:
   - List of entries sorted by most recent first
   - Each entry displays:
     - URL (clickable)
     - Why Interesting text
     - Notes (shown/hidden on click)
   - Edit and Delete buttons for each entry
   - Navigation to input page

### Functionality
- URL validation for new entries
- Edit capability for all fields
- Delete with confirmation popup
- No authentication required (local usage only)
- Unicode support for multiple languages (including Russian)
- Centralized error display location
- No success messages required

### Non-Requirements
- No search/filter functionality
- No URL availability checking
- No keyboard shortcuts
- No custom copy functionality
- No specific port number requirements

## Technical Requirements
- Flask framework
- SQLite database
- Browser's default functionality for link handling
- Support for Unicode/international character sets

## Testing Requirements
- URL validation
- CRUD operations
- Character encoding (especially Russian text)
- Form submission with required/optional fields
- Edit/delete functionality
- Error handling

This specification aims to create a minimal, functional link management system focusing on ease of use and data integrity.
