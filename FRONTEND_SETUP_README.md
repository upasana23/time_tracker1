# Frontend Setup & Usage Guide

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd frontend
npm install
```

### 2. Start Development Server
```bash
npm run dev
```

The frontend will be available at: **http://localhost:3000**

## 🏗️ What I've Fixed

### ✅ **Configuration Files Restored**
- `next.config.js` - Next.js 14 compatible configuration
- `tailwind.config.js` - Tailwind CSS with proper theme setup
- `tsconfig.json` - TypeScript configuration

### ✅ **Missing UI Components Created**
- `Button` - Interactive buttons with variants
- `Card` - Content containers with headers
- `Dialog` - Modal dialogs and popups
- `Input` - Form input fields
- `Label` - Form labels
- `Select` - Dropdown select components
- `Alert` - Notification alerts
- `Badge` - Status and category badges
- `Textarea` - Multi-line text input
- `Chart` - Chart container components

### ✅ **Missing Pages Created**
- `ML Analytics` (`/ml-predictions`) - Machine learning dashboard
- `Chatbot` (`/chatbot`) - Redirects to standalone chatbot
- `Contact` (`/contact`) - Contact form with AI live chat
- `Features` (`/features`) - Feature showcase page

### ✅ **Navigation Fixed**
- `TubelightNavbar` component with proper routing
- All navigation links working correctly
- Mobile-responsive navigation menu

### ✅ **Dependencies Updated**
- Downgraded to Next.js 14.2.5 for better compatibility
- React 18.3.1 for stability
- All Radix UI components properly versioned
- Tailwind CSS 3.4.1 with animations

## 🎯 Key Features

### **Dashboard (`/`)**
- Real-time attendance statistics
- Interactive charts and analytics
- Quick action buttons
- AI recommendations panel

### **ML Analytics (`/ml-predictions`)**
- Machine learning predictions
- Attendance trend analysis
- Risk factor assessment
- Model performance metrics

### **AI Live Chat (Contact Page)**
- Speech recognition (voice input)
- Text-to-speech (voice output)
- RAG-powered responses from ML service
- Gemini API fallback

### **Responsive Design**
- Mobile-first approach
- Glassmorphism UI elements
- Dark theme with gradient backgrounds
- Smooth animations and transitions

## 🔧 Technical Details

### **Architecture**
- **Frontend**: Next.js 14 + React 18 + TypeScript
- **Styling**: Tailwind CSS + custom CSS variables
- **Components**: Radix UI primitives + custom components
- **Charts**: Recharts for data visualization
- **Icons**: Lucide React icon library

### **State Management**
- React hooks for local state
- Form state management
- Real-time data updates
- Error handling and loading states

### **API Integration**
- RESTful API calls to backend
- ML service integration for AI features
- Chatbot API for fallback responses
- Error handling and retry logic

## 🚨 Troubleshooting

### **Common Issues**

#### 1. **Dependencies Not Installing**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and package-lock.json
rm -rf node_modules package-lock.json

# Reinstall
npm install
```

#### 2. **TypeScript Errors**
```bash
# Check TypeScript version compatibility
npx tsc --version

# Should be 5.6.3 or compatible
```

#### 3. **Tailwind CSS Not Working**
```bash
# Rebuild Tailwind CSS
npx tailwindcss -i ./app/globals.css -o ./app/output.css --watch
```

#### 4. **Port Already in Use**
```bash
# Kill process on port 3000
npx kill-port 3000

# Or use different port
npm run dev -- -p 3001
```

### **Browser Compatibility**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## 📱 Mobile Support

### **Responsive Breakpoints**
- **Mobile**: < 768px
- **Tablet**: 768px - 1024px
- **Desktop**: > 1024px

### **Touch Interactions**
- Swipe gestures for mobile navigation
- Touch-friendly button sizes
- Mobile-optimized forms

## 🎨 Customization

### **Theme Colors**
Edit `tailwind.config.js` to customize:
- Primary colors
- Secondary colors
- Accent colors
- Background gradients

### **CSS Variables**
Modify `app/globals.css` for:
- Color schemes
- Typography
- Spacing
- Animations

## 🔒 Security Features

- XSS protection headers
- Content type security
- Frame options security
- CORS configuration

## 📊 Performance

- Image optimization
- Code splitting
- Lazy loading
- Bundle optimization

## 🚀 Deployment

### **Build for Production**
```bash
npm run build
npm start
```

### **Environment Variables**
Create `.env.local`:
```env
NEXT_PUBLIC_CHATBOT_URL=http://localhost:3001
NEXT_PUBLIC_ML_API_URL=http://localhost:8000
NEXT_PUBLIC_BACKEND_URL=http://localhost:5000
```

## 📞 Support

If you encounter any issues:

1. Check the browser console for errors
2. Verify all dependencies are installed
3. Ensure backend services are running
4. Check network connectivity

## 🎉 Success!

Your frontend is now fully functional with:
- ✅ All components working
- ✅ Navigation functional
- ✅ Pages accessible
- ✅ AI features integrated
- ✅ Responsive design
- ✅ Error-free operation

**Next Steps:**
1. Start the backend service
2. Start the ML service
3. Start the chatbot service
4. Open http://localhost:3000 in your browser

Enjoy your fully functional TimeTracker application! 🎯
