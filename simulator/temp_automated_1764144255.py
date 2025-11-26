
import asyncio
import sys
import os
import json

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import simulator_wqb

async def run_automated():
    """Run the automated simulator with parameters from web interface"""
    try:
        # Load JSON data
        with open(r"C:\Users\聊城市中医医院\AppData\Local\Programs\Python\Python312\Lib\site-packages\cnhkmcp\untracked\APP\simulator\temp_expressions_1764144255.json", 'r', encoding='utf-8') as f:
            json_content = f.read()
        
        # Call automated_main with parameters
        result = await simulator_wqb.automated_main(
            json_file_content=json_content,
            username="jiacobi@163.com",
            password="jjqJJQ1324",
            start_position=0,
            concurrent_count=3,
            random_shuffle=False,
            use_multi_sim=False,
            alpha_count_per_slot=3
        )
        
        if result['success']:
            print("\n" + "="*60)
            print("🎉 WEB INTERFACE AUTOMATION SUCCESS 🎉")
            print("="*60)
            print(f"✅ Total simulations: {result['results']['total']}")
            print(f"✅ Successful: {result['results']['successful']}")
            print(f"❌ Failed: {result['results']['failed']}")
            if result['results']['alphaIds']:
                print(f"📊 Generated {len(result['results']['alphaIds'])} Alpha IDs")
            print("="*60)
        else:
            print("\n" + "="*60)
            print("❌ WEB INTERFACE AUTOMATION FAILED")
            print("="*60)
            print(f"Error: {result['error']}")
            print("="*60)
            
    except Exception as e:
        print(f"\n❌ Script execution error: {e}")
    
    finally:
        # Clean up temporary files
        try:
            if os.path.exists(r"C:\Users\聊城市中医医院\AppData\Local\Programs\Python\Python312\Lib\site-packages\cnhkmcp\untracked\APP\simulator\temp_expressions_1764144255.json"):
                os.remove(r"C:\Users\聊城市中医医院\AppData\Local\Programs\Python\Python312\Lib\site-packages\cnhkmcp\untracked\APP\simulator\temp_expressions_1764144255.json")
            if os.path.exists(r"C:\Users\聊城市中医医院\AppData\Local\Programs\Python\Python312\Lib\site-packages\cnhkmcp\untracked\APP\simulator\temp_automated_1764144255.py"):
                os.remove(r"C:\Users\聊城市中医医院\AppData\Local\Programs\Python\Python312\Lib\site-packages\cnhkmcp\untracked\APP\simulator\temp_automated_1764144255.py")
            if os.path.exists(r"C:\Users\聊城市中医医院\AppData\Local\Programs\Python\Python312\Lib\site-packages\cnhkmcp\untracked\APP\simulator\temp_run_1764144255.bat"):
                os.remove(r"C:\Users\聊城市中医医院\AppData\Local\Programs\Python\Python312\Lib\site-packages\cnhkmcp\untracked\APP\simulator\temp_run_1764144255.bat")
        except:
            pass
        
        print("\n🔄 Press any key to close this window...")
        input()

if __name__ == '__main__':
    asyncio.run(run_automated())
