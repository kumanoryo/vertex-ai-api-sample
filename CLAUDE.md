# CLAUDE.md

このファイルは、このリポジトリでコードを扱う際にClaude Code (claude.ai/code) にガイダンスを提供します。

## プロジェクト概要

Google Cloud Vertex AIの生成AI API（Geminiモデル）の基本的な使用方法を示すPythonサンプルプロジェクトです。Vertex AIクライアントの初期化とGemini 2.0 Flashモデルを使用したコンテンツ生成の簡単な例を提供します。

## 環境設定

プロジェクトには環境変数の設定が必要です：
- `.env.example`を`.env`にコピーして以下を設定：
  - `GOOGLE_CLOUD_PROJECT`: Google CloudプロジェクトID
  - `GOOGLE_API_KEY`: Vertex AIアクセス用のGoogle APIキー

## 依存関係

Pythonの依存関係をインストール：
```bash
pip install -r requirements.txt
```

主要な依存関係：
- `google-cloud-aiplatform`: Google Cloud Vertex AI SDK
- `python-dotenv`: 環境変数管理
- `requests`: HTTPライブラリ

## サンプルの実行

メインサンプルスクリプトを実行：
```bash
python vertex_ai_sample.py
```

スクリプトは以下を実行します：
1. `.env`から環境変数を読み込み
2. プロジェクト設定でVertex AIを初期化
3. Gemini 2.0 Flashモデルを読み込み
4. テストプロンプトを送信してレスポンスを表示

## アーキテクチャ

- `vertex_ai_sample.py`: Vertex AI初期化と基本的なコンテンツ生成例を含むメインエントリーポイント
- 環境設定は`.env`ファイルで処理（コミット対象外）
- APIキー不足や初期化失敗時のエラーハンドリング